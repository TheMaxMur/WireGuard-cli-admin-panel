# WireGuard cli admin panel

## Instalation

#### Dependencies
```bash
sudo apt install docker.io docker-compose
```

#### Clone repository:
``` bash 
git clone https://github.com/TheMaxMur/WireGuard-cli-admin-panel
cd WireGuard-cli-admin-panel
```

#### Usage:
Program run as root user
```
sudo python3 /path/to/repo/api_docker_vpn.py
```

#### Configuration
Config file path (Creating after first running) - /etc/wireguard_api_client/wg_api.conf

Parameters:

*workdir* - Path to wireguard folder with compose file. Default value - /path/to/repo/WireGuard-cli-admin-panel/

Example:

```
[files]
workdir = /home/user/WireGuard-cli-admin-panel/
```

