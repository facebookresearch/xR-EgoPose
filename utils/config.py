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


def set_action():
    """Clastering specialized actions in groups

    Returns:
        dict -- action names mapping
    """

    _NAMES = [
        'Gesticuling', 'Reacting', 'Greeting',
        'Talking', 'UpperStretching', 'Gaming',
        'LowerStretching', 'Patting', 'Walking', 'All'
    ]

    _ACTION = {
        'anim_Clip1': 8, 'Opening_A_Lid': 0, 'Dribble': 5, 'Boxing': 5,
        'Standing_Arguing__1_': 3, 'Happy': 3, 'Plotting': 3, 'Counting': 4,
        'Standing_Arguing': 0, 'Standing_2H_Cast_Spell_01': 4, 'Shooting_Gun': 5,
        'Two_Hand_Spell_Casting': 0, 'Shaking_Hands_2': 2, 'Hands_Forward_Gesture': 2,
        'Rifle_Punch': 1, 'Baseball_Umpire': 5, 'Angry_Gesture': 0, 'Waving_Gesture': 0,
        'Taunt_Gesture': 0, 'Golf_Putt_Failure': 5, 'Rejected': 1, 'Shake_Fist': 2,
        'Revealing_Dice': 5, 'Golf_Putt_Failure__1_': 5, 'No': 3, 'Angry_Point': 1,
        'Agreeing': 3, 'Sitting_Thumbs_Up': 6, 'Standing_Thumbs_Up': 4, 'Patting': 7,
        'Petting': 7, 'Petting_Animal': 7, 'Taking_Punch': 0,
        'Standing_1H_Magic_Attack_01': 4, 'Talking': 3, 'Standing_Greeting': 2,
        'Happy_Hand_Gesture': 0, 'Dismissing_Gesture': 1, 'Strong_Gesture': 1,
        'Pointing_Gesture': 1, 'Golf_Putt_Victory': 5, 'Pointing': 0,
        'Thinking': 4, 'Loser': 1, 'Reaching_Out': 3, 'Crazy_Gesture': 0,
        'Golf_Putt_Victory__1_': 5, 'Insult': 3, 'Arm_Gesture': 0,
        'Beckoning': 1, 'Charge': 5, 'Weight_Shift_Gesture': 8,
        'Pain_Gesture': 1, 'Fist_Pump': 0, 'Terrified': 1, 'Surprised': 1,
        'Clapping': 1, 'Rallying': 1, 'Hand_Raising': 0, 'Sitting_Disapproval': 6,
        'Quick_Formal_Bow': 2, 'Counting__1_': 0, 'Tpose_Take_001': 4,
        'upper_stretching': 4, 'lower_stretching': 6, 'walking': 8
    }

    action_map = {}
    for k, v in _ACTION.items():
        action_map[k] = _NAMES[v]

    return action_map


def load_config():
    """Load config"""

    with open('data/config.yml') as fin:
        conf = edict(yaml.safe_load(fin))

    j = set_skeleton()
    conf['skel'] = j

    act = set_action()
    conf['actions'] = act

    return conf


config = load_config()
