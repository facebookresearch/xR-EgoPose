# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# -*- coding: utf-8 -*-
"""
Demo code

@author: Denis Tome'

"""
from torch.utils.data import DataLoader
from torchvision import transforms
from base import SetType
import dataset.transform as trsf
from dataset import Mocap
from utils import config, ConsoleLogger
from utils import evaluate, io

LOGGER = ConsoleLogger("Main")


def main():
    """Main"""

    LOGGER.info('Starting demo...')

    # ------------------- Data loader -------------------

    data_transform = transforms.Compose([
        trsf.ImageTrsf(),
        trsf.Joints3DTrsf(),
        trsf.ToTensor()])

    # let's load data from validation set as example
    data = Mocap(
        config.dataset.val,
        SetType.VAL,
        transform=data_transform)
    data_loader = DataLoader(
        data,
        batch_size=config.data_loader.batch_size,
        shuffle=config.data_loader.shuffle)

    # ------------------- Evaluation -------------------

    eval_body = evaluate.EvalBody()
    eval_upper = evaluate.EvalUpperBody()
    eval_lower = evaluate.EvalUpperBody()

    # ------------------- Read dataset frames -------------------

    for it, (img, p2d, p3d, action) in enumerate(data_loader):

        LOGGER.info('Iteration: {}'.format(it))
        LOGGER.info('Images: {}'.format(img.shape))
        LOGGER.info('p2ds: {}'.format(p2d.shape))
        LOGGER.info('p3ds: {}'.format(p3d.shape))
        LOGGER.info('Actions: {}'.format(action))

        # -----------------------------------------------------------
        # ------------------- Run your model here -------------------
        # -----------------------------------------------------------

        # TODO: p3d_hat is model's predition

        # Evaluate results using different evaluation metrices
        y_output = p3d_hat.data.cpu().numpy()
        y_target = p3d.data.cpu().numpy()

        eval_body.eval(y_output, y_target, action)
        eval_upper.eval(y_output, y_target, action)
        eval_lower.eval(y_output, y_target, action)

    # ------------------- Save results -------------------

    LOGGER.info('Saving evaluation results...')
    res = {'FullBody': eval_body.get_results(),
           'UpperBody': eval_upper.get_results(),
           'LowerBody': eval_lower.get_results()}

    io.write_json(config.eval.output_file, res)

    LOGGER.info('Done.')


if __name__ == "__main__":
    main()
