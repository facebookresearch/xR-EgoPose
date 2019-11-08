# -*- coding: utf-8 -*-
"""
Demo code

@author: Denis Tome'

"""
from torchvision import transforms
from base import SetType
import dataset.transform as trsf
from dataset import Mocap
from utils import config


# db = Mocap(config.dataset.val, SetType.VAL)
data_transform = transforms.Compose([
    trsf.ImageTrsf(),
    trsf.Joints3DTrsf(),
    trsf.ToTensor()
])
db = Mocap('data/Dataset/Tmp',
           SetType.VAL,
           transform=data_transform)
db.__getitem__(0)
