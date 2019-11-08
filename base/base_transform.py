# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# -*- coding: utf-8 -*-
"""
Base Transform class

@author: Denis Tome'

"""
from abc import ABC, abstractmethod
from utils import ConsoleLogger


class BaseTransform(ABC):
    """BaseTrasnform class"""

    def __init__(self):
        super().__init__()
        self.logger = ConsoleLogger(self.__class__.__name__)

    @abstractmethod
    def __call__(self, data):
        """Perform transformation

        Arguments:
            data {dict} -- frame data
        """
        raise NotImplementedError
