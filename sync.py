import json
from os import system


def sync():
    upnp_list = json.load(open('database.json', 'r'))
    for remote_port in upnp_list.keys():
        upnp = upnp_list[remote_port]
        local_port = upnp['local_port']
        remote_port = upnp['remote_port']
        protocol = upnp['protocol']
        ip = upnp['ip']
        system(f'upnpc -a {ip} {local_port} {remote_port} {protocol}')

if __name__ == '__main__':
    sync()
