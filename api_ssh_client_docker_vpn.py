#!/bin/python3
import os
import subprocess

hostname = 'user@hostname'
ip = hostname.split("@")
ip = list(hostname[1])
start_message = "\033[36mWireGuard PREgenerator from MaxMur ver 0.1\033[0m" 
list_to_messa = ("\n            l - show list of users in peer section" +
            "\n            r - raplace list of users in peer selection with existing file" +
            "\n            d - delete user by its id" +
            "\n            a - append list of users" +
            "\n            b - make backup of existing yaml (/opt/wireguatd-server/docker-compose.yaml)" +
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

print(start_message)
print(list_to_messa)
while True:
    choice = str(input("\033[33m(menu)\033[0m Enter: "))
    if choice == "q":
        break
    elif choice == "m":
        print(list_to_messa)
    elif choice == "s":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py s'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "I":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py I'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "S":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py S'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "R":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py R'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "P":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py P'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "b":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py b'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "l":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py l'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "D":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py D'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "":
        continue
    elif choice == "c":
        os.system("clear")
    elif choice == "d":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py d'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "a":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py a'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == "A":
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py A'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    elif choice == 'r':
        cmd = "ssh " + hostname + " -t 'cd /opt/wireguard-server/ && sudo python3 /opt/wireguard-server/api_ssh_server_docker_vpn.py r'"
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        output = result.communicate()[0]
        output = output[:-38-(len(ip))]
        print(output)
    else:
        print('Wrong operation! Enter "m" to show list of commands')
