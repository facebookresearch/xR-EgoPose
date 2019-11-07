# -*- coding: utf-8 -*-
"""
Data processing where only Images and associated 3D
joint positions are loaded.

@author: Denis Tome'

"""
import os
from skimage import io as sio
import numpy as np
from base import BaseDataset
from utils import io


class Mocap(BaseDataset):
    """Mocap Dataset loader"""

    ROOT_DIRS = ['rgba', 'json']

    def index_db(self):

        return self._index_dir(self.path)

    def _index_dir(self, path):
        """Recursively add paths to the set of
        indexed files

        Arguments:
            path {str} -- folder path

        Returns:
            dict -- indexed files per root dir
        """

        indexed_paths = dict()
        sub_dirs, _ = io.get_subdirs(path)
        if set(self.ROOT_DIRS) <= set(sub_dirs):

            # get files from subdirs
            n_frames = -1

            # let's extract the rgba and json data per frame
            for sub_dir in self.ROOT_DIRS:
                d_path = os.path.join(path, sub_dir)
                _, paths = io.get_files(d_path)

                if n_frames < 0:
                    n_frames = len(paths)
                else:
                    if len(paths) != n_frames:
                        self.logger.error(
                            'Frames info in {} not matching other passes'.format(d_path))

                indexed_paths.update({sub_dir: paths})

            return indexed_paths

        # initialize indexed_paths
        for sub_dir in self.ROOT_DIRS:
            indexed_paths.update({sub_dir: []})

        # check subdirs of path and merge info
        for sub_dir in sub_dirs:
            indexed = self._index_dir(os.path.join(path, sub_dir))

            for r_dir in self.ROOT_DIRS:
                indexed_paths[r_dir].extend(indexed[r_dir])

        return indexed_paths

    def _process_points(self, data):

        p2d_orig = np.array(data['pts2d_fisheye']).T
        p3d_orig = np.array(data['pts3d_fisheye']).T
        joint_names = {j['name'].replace('mixamorig:', ''): jid
                       for jid, j in enumerate(data['joints'])}

        # ------------------- Filter joints -------------------
        

    def __getitem__(self, index):

        # load image
        img_path = self.index['rgba'][index].decode('utf8')
        img = sio.imread(img_path).astype(np.float32)
        img /= 255.0

        # read joint positions
        json_path = self.index['json'][index].decode('utf8')
        data = io.read_json(json_path)
        p2d, p3d = self._process_points(data)

        # TODO: return action as well

        return -1

    def __len__(self):

        return len(self.index[self.ROOT_DIRS[0]])
