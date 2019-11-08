# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# -*- coding: utf-8 -*-
"""
Base class for datasets.

This code assumes that the dataset structure is the one
provided in the README.md file.

@author: Denis Tome'

"""
import os
import enum
from torchvision import transforms
from torch.utils.data import Dataset
from base import BaseTransform
from utils import ConsoleLogger, io


class SetType(enum.Enum):
    """Set types"""

    TRAIN = 'train_set'
    VAL = 'val_set'
    TEST = 'test_set'


class BaseDataset(Dataset):
    """
    Base class for all datasets
    """

    def __init__(self, db_path, set_type, transform=None):
        """Init class

        Arguments:
            db_path {str} -- path to set
            set_type {SetType} -- set

        Keyword Arguments:
            transform {BaseTransform} -- transformation to apply to data (default: {None})
        """

        assert isinstance(set_type, SetType)
        self.logger = ConsoleLogger(set_type.value)

        if io.exists(db_path):
            self.path = db_path
        else:
            self.logger.error('Dataset directory {} not found'.format(db_path))

        self.index = self._load_index()

        if transform:
            assert isinstance(transform, (BaseTransform, transforms.Compose))
        self.transform = transform

    def _load_index(self):
        """Get indexed set. If the set has already been
        indexed, load the file, otherwise index it and save cache.

        Returns:
            dict -- index set
        """

        idx_path = os.path.join(self.path, 'index.h5')
        if io.exists(idx_path):
            return io.read_h5(idx_path)

        index = self.index_db()
        io.write_h5(idx_path, index)
        return index

    def index_db(self):
        """Index data for faster execution"""

        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
