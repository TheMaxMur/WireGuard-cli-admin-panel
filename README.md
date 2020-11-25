# WireGuard cli admin panel

### Installation for use in server:

For first connect your server.

#### Clone repository:
``` bash 
$ git clone https://github.com/TheMaxMur/WireGuard-cli-admin-panel
$ cd WireGuard-cli-admin-panel
```
#### Install wireguard in docker:

**If you have already install wireguard in docker dont use script, just move api_docker_vpn.py in folder with docker-compose.yaml.**

``` bash
$ chmod +x script.sh
$ sudo bash script.sh
```

#### Edit path to files:
So, you install docker with wg in your server, now need create a client:
* edit path_to_yaml_file in api_docker_vpn.py

#### Usage:
Programm run as root user
```
# python3 /opt/wireguard/api_docker_vpn.py
```

### Instalatlion for remote use in server:

For first connect your server.

#### Clone repository:
``` bash
$ git clone https://github.com/TheMaxMur/WireGuard-cli-admin-panel
$ cd WireGuard-cli-admin-panel
```
#### Install wireguard in docker:

**If you have already install wireguard in docker dont use script, just move api_ssh_server_docker_vpn.py in folder with docker-compose.yaml.**

``` bash
$ chmod +x script.sh
$ sudo bash script.sh
```

This script install wireguard in docker from dockerhub. Absolutely necessary read [this documentation](https://hub.docker.com/r/linuxserver/wireguard), and config your .yaml file.

#### Configure ssh-keygen and sudo access:
For first, run ssh-keygen in your client:
``` bash
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ylo/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/ylo/.ssh/id_rsa.
Your public key has been saved in /home/ylo/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:Up6KjbnEV4Hgfo75YM393QdQsK3Z0aTNBz0DoirrW+c ylo@klar
The key's randomart image is:
+---[RSA 2048]----+
|    .      ..oo..|
|   . . .  . .o.X.|
|    . . o.  ..+ B|
|   .   o.o  .+ ..|
|    ..o.S   o..  |
|   . %o=      .  |
|    @.B...     . |
|   o.=. o. . .  .|
|    .oo  E. . .. |
+----[SHA256]-----+
klar (11:40) ~>
```
``` bash
$ ssh-copy-id user@host
```

For using api in normal mode you want to create a new user which can use sudo without password.
``` bash
$ sudo useradd -g users -G sudo username
```
Edit /etc/sudores
``` bash
$ sudo vim /etc/sudores
```

```
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults	env_reset
Defaults	mail_badpass
Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root	ALL=(ALL:ALL) ALL
username ALL=(ALL) NOPASSWD: ALL #!!!new string with access!!! 

# Allow members of group sudo to execute any command
%sudo	ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d

```

#### Edit path to files, hostnames.

So, you install docker with wg in your server, now need create a client:
* edit path_to_yaml_file in api_ssh_server_docker_vpn.py
* edit hostname in api_ssh_client_docker_vpn.py
* edit path_to_wireguard_docker_dir in apt_ssh_client_docker_vpn.py
* copy api_ssh_client_docker_vpn.py on your client pc

#### Usage:
Just run api_ssh_client_docker_vpn.py in your client pc
```bash
$ python3 api_ssh_client_docker_vpn.py
```
