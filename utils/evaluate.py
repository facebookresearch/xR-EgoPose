# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# -*- coding: utf-8 -*-
"""
Class for model evaluation

@author: Denis Tome'

"""
import numpy as np
from base import BaseEval

__all__ = [
    'EvalBody',
    'EvalUpperBody',
    'EvalLowerBody'
]


def compute_error(pred, gt):
    """Compute error

    Arguments:
        pred {np.ndarray} -- format (N x 3)
        gt {np.ndarray} -- format (N x 3)

    Returns:
        float -- error
    """

    if pred.shape[1] != 3:
        pred = np.transpose(pred, [1, 0])

    if gt.shape[1] != 3:
        gt = np.transpose(gt, [1, 0])

    assert pred.shape == gt.shape
    error = np.sqrt(np.sum((pred - gt)**2, axis=1))

    return np.mean(error)


class EvalBody(BaseEval):
    """Eval entire body"""

    def eval(self, pred, gt, actions=None):
        """Evaluate

        Arguments:
            pred {np.ndarray} -- predictions, format (N x 3)
            gt {np.ndarray} -- ground truth, format (N x 3)

        Keyword Arguments:
            action {str} -- action name (default: {None})
        """

        for pid, (pose_in, pose_target) in enumerate(zip(pred, gt)):
            err = compute_error(pose_in, pose_target)

            if actions:
                act_name = self._map_action_name(actions[pid])

                # add element to dictionary if not there yet
                if not self._is_action_stored(act_name):
                    self._init_action(act_name)
                self.error[act_name].append(err)

            # add to all
            act_name = 'All'
            self.error[act_name].append(err)

    def desc(self):
        return 'Average3DError'


class EvalUpperBody(BaseEval):
    """Eval upper body"""

    _SEL = [4, 5, 6, 7, 8, 9, 10, 11]

    def eval(self, pred, gt, actions=None):
        """Evaluate

        Arguments:
            pred {np.ndarray} -- predictions, format (N x 3)
            gt {np.ndarray} -- ground truth, format (N x 3)

        Keyword Arguments:
            action {str} -- action name (default: {None})
        """

        for pid, (pose_in, pose_target) in enumerate(zip(pred, gt)):
            err = compute_error(pose_in[self._SEL], pose_target[self._SEL])

            if actions:
                act_name = self._map_action_name(actions[pid])

                # add element to dictionary if not there yet
                if not self._is_action_stored(act_name):
                    self._init_action(act_name)
                self.error[act_name].append(err)

            # add to all
            act_name = 'All'
            self.error[act_name].append(err)

    def desc(self):
        return 'UpperBody_Average3DError'


class EvalLowerBody(BaseEval):
    """Eval lower body"""

    _SEL = [0, 1, 2, 3, 12, 13, 14, 15]

    def eval(self, pred, gt, actions=None):
        """Evaluate

        Arguments:
            pred {np.ndarray} -- predictions, format (N x 3)
            gt {np.ndarray} -- ground truth, format (N x 3)

        Keyword Arguments:
            action {str} -- action name (default: {None})
        """

        for pid, (pose_in, pose_target) in enumerate(zip(pred, gt)):
            err = compute_error(pose_in[self._SEL], pose_target[self._SEL])

            if actions:
                act_name = self._map_action_name(actions[pid])

                # add element to dictionary if not there yet
                if not self._is_action_stored(act_name):
                    self._init_action(act_name)
                self.error[act_name].append(err)

            # add to all
            act_name = 'All'
            self.error[act_name].append(err)

    def desc(self):
        return 'LowerBody_Average3DError'
