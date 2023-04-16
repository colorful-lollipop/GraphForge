r"""
import config file
"""
import logging
import os

import yaml


class GraphDB:
    type: str = 'Nebula Graph'
    ip: str = '127.0.0.1'
    port: int = '9669'
    username: str = 'root'
    password: str = 'nebula'


def load_config(file: str = 'config.yml'):
    if not os.path.isfile(file):
        return
    with open(file, 'r') as f:
        d = yaml.full_load(f.read())
    cfg = d['GraphDB']
    for attr in dir(GraphDB):
        setattr(GraphDB, attr, cfg[attr])
