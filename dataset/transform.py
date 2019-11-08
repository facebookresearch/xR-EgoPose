# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# -*- coding: utf-8 -*-
"""
Transformation to apply to the data

@author: Denis Tome'

"""
import torch
import numpy as np
from base import BaseTransform
from utils import config


class ImageTrsf(BaseTransform):
    """Image Transform"""

    def __init__(self, mean=0.5, std=0.5):

        super().__init__()
        self.mean = mean
        self.std = std

    def __call__(self, data):
        """Perform transformation

        Arguments:
            data {dict} -- frame data
        """

        if 'image' not in list(data.keys()):
            return data

        # get image from all data
        img = data['image']

        # channel last to channel first
        img = np.transpose(img, [2, 0, 1])

        # normalization
        img -= self.mean
        img /= self.std
        data.update({'image': img})

        return data


class Joints3DTrsf(BaseTransform):
    """Joint Transform"""

    def __init__(self):

        super().__init__()
        joint_zeroed = config.transforms.norm

        assert joint_zeroed in config.skel.keys()
        self.jid_zeroed = config.skel[joint_zeroed].jid

    def __call__(self, data):
        """Perform transformation

        Arguments:
            data {dict} -- frame data
        """

        if 'joints3D' not in list(data.keys()):
            return data

        p3d = data['joints3D']
        joint_zeroed = p3d[self.jid_zeroed][np.newaxis]

        # update p3d
        p3d -= joint_zeroed
        data.update({'joints3D': p3d})

        return data


class ToTensor(BaseTransform):
    """Convert ndarrays to Tensors."""

    def __call__(self, data):
        """Perform transformation

        Arguments:
            data {dict} -- frame data
        """

        keys = list(data.keys())
        for k in keys:
            pytorch_data = torch.from_numpy(data[k]).float()
            data.update({k: pytorch_data})

        return data
