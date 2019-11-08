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

LOGGER = ConsoleLogger("Main")


def main():
    """Main"""

    LOGGER.info('Starting demo...')

    # ------------------- Data loader -------------------

    data_transform = transforms.Compose([
        trsf.ImageTrsf(),
        trsf.Joints3DTrsf(),
        trsf.ToTensor()])

    # let's load data from validation set
    data = Mocap(
        config.dataset.val,
        SetType.VAL,
        transform=data_transform)
    data_loader = DataLoader(
        data,
        batch_size=config.data_loader.batch_size,
        shuffle=config.data_loader.shuffle)

    # ------------------- Read data -------------------

    for it, (img, p2d, p3d, action) in enumerate(data_loader):

        LOGGER.info('Iteration: {}'.format(it))
        LOGGER.info('Images: {}'.format(img.shape))
        LOGGER.info('p2ds: {}'.format(p2d.shape))
        LOGGER.info('p3ds: {}'.format(p3d.shape))
        LOGGER.info('Actions: {}'.format(action))

        # -----------------------------------------------------
        # ------------------- Run you model -------------------
        # -----------------------------------------------------

        #TODO: add evaluation code

        break

    LOGGER.info('Done')


if __name__ == "__main__":
    main()
