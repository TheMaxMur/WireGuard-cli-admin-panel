#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import yaml
import getpass
import pathlib
import subprocess
import configparser

def add_slash(string: str="") -> str:
    if string[-1] != '/':
        return (string + '/')

    return (string + '/')

def compose_file_extension(path: str="") -> str:
    if os.path.isfile(path + 'docker-compose.yaml'):
        return (path + 'docker-compose.yaml')
    if os.path.isfile(path + 'docker-compose.yml'):
        return (path + 'docker-compose.yml')

    return ("")

def initializaion_config() -> None:
    try:
        file = open(config_dir + 'wg_api.conf')
        file.close()
    except:
        config['files'] = {}
        workdir = input("Enter wireguard docker-compose workdir: ")
        if workdir == "":
            workdir = os.path.abspath(os.path.dirname(__file__))
            print(workdir)
        config['files']['workdir'] = workdir
        config['files']['workdir'] = add_slash(config['files']['workdir'])

        with open(config_dir + 'wg_api.conf', 'w') as configfile:
            config.write(configfile)

username = getpass.getuser()

if username == 'root':
    pass
else:
    print("\033[36m---------------------------------------\033[0m")
    print("\033[31m               NEED ROOT\033[0m")
    print("\033[36m---------------------------------------\033[0m")
    exit()

config_dir = '/etc/wireguard_api_client/'
pathlib.Path(config_dir).mkdir(parents=True, exist_ok=True)
config = configparser.ConfigParser()
initializaion_config()

config.read(config_dir + 'wg_api.conf')

wg_dir = add_slash(config['files']['workdir'])
path_to_config_folder = wg_dir + 'config/'
path_to_yaml_file = ""

if compose_file_extension(wg_dir) != "":
    path_to_yaml_file = compose_file_extension(wg_dir)
else:
    print("\033[31mCOMPOSE FILE NOT FOUND\033[0m")
    exit()
    """choice = input("\nEnter another path? (y/n): ")

    if choice == "y":
        initializaion_config()
    else:
        exit()"""

start_message = "\033[36mWireGuard PREgenerator from MaxMur ver 0.2.2\033[0m" 
list_to_messa = ("\n            l - show list of users in peer section" +
            "\n            r - raplace list of users in peer selection with existing file" +
            "\n            d - delete user by its id" +
            "\n            a - append list of users" +
            "\n            b - make backup of existing yaml (" + path_to_yaml_file + ")" +
            "\n            m - show this menu" +
            "\n            s - show yaml config file" +
            "\n            c - clear terminal"
            "\n            A - show active users" + 
            "\n            I - rebuild/init WireGuard docker" +
            "\n            S - start WireGuard docker" + 
            "\n            R - restart WireGuard docker" +
            "\n            P - poweroff WireGuard docker" +
            "\n            D - show Docker state" +
            "\n            q - quit\n")

def transliterate(name):
   slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ya', ',':'','?':'',' ':'','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e', '—':''}
        
   for key in slovar:
      name = name.replace(key, slovar[key])
   return name

def command_shell(cmd: str="", choice: str="") -> list:
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]

        if choice != "":
            massive = output.split("\n")
        else:
            massive = output.split(",")
            massive[-1] = massive[-1].split("#")[0]

        return (massive)

def edit_peers(massive: list=[]) -> list:
    for i in range(len(massive)):
        if i == 0:
            del_peers = massive[i].split("=")
            massive[i] = del_peers[1]

        if i == len(massive)-1:
            last_peer = massive[i]
            last_peer = last_peer[:-1]
            massive[i] = last_peer.rstrip()
    return (massive)

def edit_yaml_file(peers: str="") -> None:
    content = {}

    with open(path_to_yaml_file, "r") as name_file:
        try:
            content = yaml.safe_load(name_file)
        except yaml.YAMLError as yerror:
            print(yerror)
    content["services"]["wireguard"]["environment"][5] = peers

    with open(path_to_yaml_file, 'w') as f:
        yaml.safe_dump(content, f, default_flow_style=False)

    return (None)

def user_list(choice: str='l') -> None:
    massive = command_shell("cat " + path_to_yaml_file + " | grep PEERS | tr -d ' '")
    print("\033[36m--------------------------------------\033[0m")

    if choice == "l":
        print("\033[32mTOTAL users:\033[0m", len(massive))
    elif choice == "d":
        print("CURRENT users: ", len(massive))
    massive = edit_peers(massive)

    for i in range(len(massive)):
        print(i+1, massive[i])
    print("\033[36m--------------------------------------\033[0m")

    return (None)

def delete_user() -> None:
    choice_for_delete = 0

    try:
        choice_for_delete_massive = [int(z) for z in input("\033[33m(submenu)\033[0m IDs: ").split(',')]
    except:
        choice_for_delete_massive = []
        print('Enter NUMBER or range of number')
        delete_user()

    if len(choice_for_delete_massive) != 0:
        choice_for_delete = []
        peers = "PEERS="
        massive = command_shell("cat " + path_to_yaml_file + " | grep PEERS | tr -d ' '")
        massive = edit_peers(massive)

        for kendex in choice_for_delete_massive:
            if kendex > 0 and kendex <= len(massive):
                choice_for_delete.append(kendex)
            else:
                print('Error ID: ', kendex)

        if len(choice_for_delete) != 0:
            print("\033[31mDETELED users: \033[0m")

            for index in range(len(choice_for_delete)):
                print("\033[31m-\033[0m  " + massive[choice_for_delete[index]-1])
            user_sure = str(input("\033[31mConfirm DELETION?\033[0m <y/n>"))

            if user_sure == "y":
                for i in range(len(massive)):
                    if i+1 not in choice_for_delete:
                        peers += massive[i] + ","
                peers = peers[:-1]
                edit_yaml_file(peers)

                for j in range(len(choice_for_delete)):
                    os.system("rm -r "+ path_to_config_folder +"/peer_" + massive[choice_for_delete[j]-1] + " > /dev/null 2>&1")
                print("User deleted only in list, he anyawy can connect to vpn, if u need delete user then rebuild docker 'I'")
            else:
                print("Abort.")

    return (None)

def add_user() -> None:
    check_new_user = 0
    choice_for_add = ""
    print("\033[35mEnter usernames, e.g. 'petrov,sidorov': \033[0m")

    try:
        choice_for_add = str(input("(submenu) Users: "))
    except:
        print("Error. Try again or type q for exit")
        add_user()

    if choice_for_add != "":
        choice_for_add = choice_for_add.split(',')

        for k in range(len(choice_for_add)):
            choice_for_add[k] = choice_for_add[k].lower()
            choice_for_add[k] = transliterate(choice_for_add[k])
        peers = "PEERS="
        massive = command_shell("cat " + path_to_yaml_file + " | grep PEERS | tr -d ' '")
        massive = edit_peers(massive)

        for t in range(len(choice_for_add)):
            if choice_for_add[t] not in massive:
                massive.append(choice_for_add[t])
                check_new_user = 1
            else: 
                print('User', choice_for_add[t], 'already exist!')

        if check_new_user != 0:
            print("\033[36m---------------------------------------\033[0m")
            print("\033[32mTOTAL users:\033[0m", len(massive))
            for i in range(len(massive)):
                print(i+1, massive[i])
            print("\033[36m---------------------------------------\033[0m")
            choice_to_add = str(input("\033[31mConfirm new list?\033[0m <y/n>"))

            if choice_to_add == "y":
                for i in range(len(massive)):
                    peers += massive[i] + ','
                peers = peers[:-1]
                edit_yaml_file(peers)
                print('Users only add to list, if u need to connet this user rebuild docker "I"')
            else:
                print("Abort.")
        elif choice_for_add == "q":
            return (None)
        elif len(choice_for_add) == 1 and choice_for_add[1] == "":
            print("Error. Try again or typy q for exit")
            add_user()

    return (None)

def list_activity() -> None:
    output = command_shell("docker exec -it wireguard wg", "A")
    print()

    for i in range(len(output)):
        if "endpoint" in output[i]:
            string = output[i-2].split(" ")
            string = string[1]
            string = string[5:-4]
            user_name = ""

            with open(path_to_config_folder + "wg0.conf") as wg_conf:
                array = [row.strip() for row in wg_conf]

            for j in range(len(array)):
                if string in array[j]:
                    user_name = array[j-1]
                    user_name = user_name[7:]

            print("\033[36mUser:\033[0m", user_name)
            print(output[i])
            print(output[i+1])
            print(output[i+2])
            print(output[i+3], end="\n\n")

    return (None)

def add_users_from_list() -> None:
    array = []

    try:
        path_to_file = str(input('Enter path to list of users:'))
        if path_to_file != "q":
            with open(path_to_file) as wg_conf:
                array = [row.strip() for row in wg_conf]
    except:
        path_to_file = ""
        print('Error. Incorrect path, try again or type q for exit')
        add_users_from_list()

    if path_to_file == "q":
        return (None)
    elif path_to_file != "":
        peers = "PEERS="
        massive = command_shell("cat " + path_to_yaml_file + " | grep PEERS | tr -d ' '")
        choice_to_save = str(input("Save exist peers? <y/n>"))

        if choice_to_save == "y":
            massive = edit_peers(massive)

            for t in range(len(array)):
                massive.append(array[t])

            for i in range(len(massive)):
                peers += massive[i] + ','
            peers = peers[:-1]
            edit_yaml_file(peers)
            print('Users only add to list, if u need to connet this user rebuild docker "I"')
        elif choice_to_save == "n":
            for p in range(len(array)):
                peers += array[p]
            edit_yaml_file(peers)
            print('Users only add to list, if u need to connet this user rebuild docker "I"')
    elif path_to_file == "":
        return (None)
    else:
        print("Abort.")

    return (None)
   
def main() -> int:
    print(start_message)
    print(list_to_messa)

    while True:
        choice = str(input("\033[33m(menu)\033[0m Enter: "))
        if choice == "q":
            return (0)
        elif choice == "m":
            print(list_to_messa)
        elif choice == "s":
            print()
            os.system("cat " + path_to_yaml_file)
            print()
        elif choice == "I":
            result_command = os.system("docker-compose up -d --force-recreate")
            if result_command == 0:
                print("WireGuard REBUILD AND STARTED")
            else:
                print("Error. WireGuard not REBUILD AND STARTED")
        elif choice == "S":
            result_command = os.system("docker-compose start wireguard")
            if result_command == 0:
                print("WireGuard STARTED")
            else:
                print("Error. WireGuard not STARTED")
        elif choice == "R":
            result_command = os.system("docker-compose restart wireguard")
            if result_command == 0:
                print("WireGuard RESTARTED")
            else:
                print("Error. WireGuard not RESTARTED")
        elif choice == "P":
            result_command = os.system("docker-compose stop wireguard ")
            if result_command == 0:
                print("WireGuard STOPPED")
            else:
                print('Error. WireGuard not STOPPED.')
        elif choice == "b":
            os.system("cp " + path_to_yaml_file + " " + path_to_yaml_file + "_backup")
            print("YAML BACKUPED")
        elif choice == "l":
            user_list(choice)
        elif choice == "D":
            os.system('docker inspect wireguard --format "{{ .State.Status }}"')
        elif choice == "":
            continue
        elif choice == "c":
            os.system("clear")
        elif choice == "d":
            user_list(choice)
            delete_user()
        elif choice == "a":
            add_user()
        elif choice == "A":
            list_activity()
        elif choice == 'r':
            add_users_from_list()
        else:
            print('Wrong operation! Enter "m" to show list of commands')

    return (0)

if __name__ == '__main__':
    main()

