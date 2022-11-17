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
Programm run as root user
```
sudo python3 /path/to/repo/api_docker_vpn.py
```

#### Configuration
Config file path -- /etc/wireguard_api_client/wg_api.conf

```
[files]
workdir = /path/to/repo/WireGuard-cli-admin-panel/ # docker-compose file path. Default - /path/to/repo/WireGuard-cli-admin-panel/
```

