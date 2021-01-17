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

