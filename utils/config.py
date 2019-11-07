# -*- coding: utf-8 -*-
"""
Load data configuration

@author: Denis Tome'

"""

import yaml
from easydict import EasyDict as edict

# def set_skeleton():


def load_config():
    """Load config"""

    with open('data/config.yml') as fin:
        conf = edict(yaml.safe_load(fin))

    return conf


config = load_config()
