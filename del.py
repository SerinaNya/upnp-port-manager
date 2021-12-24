import json
from os import system

import click


@click.command()

@click.argument('remote_port')
@click.argument('protocol')
def delete(remote_port, protocol):
    system(f'upnpc -d {remote_port} {protocol}')
    upnp_list = json.load(open('database.json', 'r'))
    del upnp_list[protocol][str(remote_port)]
    json.dump(upnp_list, open('database.json', 'w'))
    click.echo(f'> DEL DONE: {remote_port} {protocol}')


if __name__ == '__main__':
    delete()
