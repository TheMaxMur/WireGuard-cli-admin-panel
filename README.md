# WireGuard cli admin panel

### Foreward:
If you need use api remote, use next instalation on your server. Else, just install on server wiregurad in docker with scritp.sh and use api_docker_vpn.py.

### Instalation for server:

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

Move api_ssh_server_docker_vpn.py in folder, where locate docker-compose.yaml (defaul dir: /opt/wireguard-server/)
```
$ sudo mv api_ssh_server_docker_vpn.py /opt/wireguard-server/
```

So, you install docker with wg in your server, now need create a client::
* copy api_ssh_server_docker_vpn.py on your client pc
* edit hostname in api_ssh_server_docker_vpn.py
