import json
from os import system

import click


@click.command()
@click.argument('vmid')
@click.argument('local_port')
@click.argument('remote_port')
@click.argument('protocol')
def add(vmid, local_port, remote_port, protocol):
    ip = f'192.168.1.{vmid}'
    system(f'upnpc -a {ip} {local_port} {remote_port} {protocol}')
    upnp_list = json.load(open('database.json', 'r'))
    upnp_list[str(remote_port)] = {
        'local_port': local_port,
        'remote_port': remote_port,
        'protocol': protocol,
        'ip': ip
    }
    json.dump(upnp_list, open('database.json', 'w'))
    click.echo(f'ADD DONE: {remote_port} {protocol}')


if __name__ == '__main__':
    add()
