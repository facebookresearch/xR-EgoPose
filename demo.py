# -*- coding: utf-8 -*-
"""
Test

@author: Denis Tome'

"""

from base import SetType
from dataset import Mocap
from utils import config


db = Mocap(config.dataset.train, SetType.TRAIN)
db.__getitem__(0)