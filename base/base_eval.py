# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# -*- coding: utf-8 -*-
"""
Base eval class

@author: Denis Tome'

"""
from abc import ABC, abstractmethod
import numpy as np
from utils import ConsoleLogger


class BaseEval(ABC):
    """BaseTrasnform class"""

    def __init__(self):
        super().__init__()
        self.logger = ConsoleLogger(self.__class__.__name__)

        self.error = {'All': []}

    def _init_action(self, action_name):
        """Add action to dictionary

        Arguments:
            action_name {str} -- action name
        """

        self.error.update({action_name: []})

    def _is_action_stored(self, action):
        """Is action already stored?

        Arguments:
            action {str} -- action name

        Returns:
            bool -- True if action is already stored
        """

        return action in self.error.keys()

    def get_results(self):
        """Get results

        Returns:
            dict -- results per action
        """

        results = {}
        for k, v in self.error.items():
            results.update({k: float(np.mean(v))})

        return results

    @abstractmethod
    def eval(self, pred, gt, actions=None):
        """Evaluate model

        Arguments:
            pred {np.ndarray} -- predicted poses
            gt {np.ndarray} -- ground truth poses

        Keyword Arguments:
            actions {str} -- action (default: {None})
        """
        raise NotImplementedError

    @abstractmethod
    def desc(self):
        """Metric description

        Returns:
            str -- short description
        """
        raise NotImplementedError
