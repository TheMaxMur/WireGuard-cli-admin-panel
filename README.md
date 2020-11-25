# WireGuard cli admin panel

### Instalation:

#### Clone repository:
```
$ git clone https://github.com/TheMaxMur/WireGuard-cli-admin-panel
$ cd WireGuard-cli-admin-panel
```
#### Script.sh:

```
$ chmod +x script.sh
$ sudo bash script.sh
```

This script install wireguard in docker from dockerhub. You can read [this documentation](https://hub.docker.com/r/linuxserver/wireguard), and config your .yaml file.

#### Edit path to files and hostnames.

So, you install docker with wg, if you need use this api remote do this:
* copy api_ssh_server_docker_vpn.py
