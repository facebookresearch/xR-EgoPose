# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# -*- coding: utf-8 -*-
"""
Load data configuration

@author: Denis Tome'

"""
import yaml
from easydict import EasyDict as edict


def set_skeleton():
    """Create skeleton definition

    Returns:
        dict -- hierarchy
    """

    joints = {
        'Hips': {'parent': None, 'col': 0},
        'Spine': {'parent': 'Hips', 'col': 0},
        'Spine1': {'parent': 'Spine', 'col': 0},
        'Spine2': {'parent': 'Spine1', 'col': 0},
        'Neck': {'parent': 'Spine2', 'col': 5},
        'Head': {'parent': 'Neck', 'col': 5},
        'LeftShoulder': {'parent': 'Spine2', 'col': 0},
        'LeftArm': {'parent': 'LeftShoulder', 'col': 3},
        'LeftForeArm': {'parent': 'LeftArm', 'col': 3},
        'LeftHand': {'parent': 'LeftForeArm', 'col': 4},
        'RightShoulder': {'parent': 'Spine2', 'col': 0},
        'RightArm':  {'parent': 'RightShoulder', 'col': 1},
        'RightForeArm':  {'parent': 'RightArm', 'col': 1},
        'RightHand':  {'parent': 'RightForeArm', 'col': 2},
        'LeftUpLeg': {'parent': 'Hips', 'col': 8},
        'LeftLeg': {'parent': 'LeftUpLeg', 'col': 8},
        'LeftFoot': {'parent': 'LeftLeg', 'col': 9},
        'LeftToeBase': {'parent': 'LeftFoot', 'col': 9},
        'RightUpLeg': {'parent': 'Hips', 'col': 6},
        'RightLeg': {'parent': 'RightUpLeg', 'col': 6},
        'RightFoot': {'parent': 'RightLeg', 'col': 7},
        'RightToeBase': {'parent': 'RightFoot', 'col': 7},
    }

    for jid, v in enumerate(joints.values()):
        v.update({'jid': jid})

    return joints


def load_config():
    """Load config"""

    with open('data/config.yml') as fin:
        conf = edict(yaml.safe_load(fin))

    j = set_skeleton()
    conf['skel'] = j

    return conf


config = load_config()
