# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# -*- coding: utf-8 -*-
"""
IO utilities

@author: Denis Tome'

"""
import os
import re
import json
import h5py
import numpy as np


__all__ = [
    'exists',
    'get_subdirs',
    'get_files',
    'write_h5',
    'read_h5',
    'write_json',
    'read_json'
]


def exists(path):
    """Check if file/directory exists

    Arguments:
        path {str} -- path

    Returns:
        bool -- True if file/dir exists
    """

    return os.path.exists(path)


def get_subdirs(path):
    """Get directories contained in path

    Arguments:
        path {str} -- path

    Returns:
        list -- directory names
        list -- directory paths
    """

    try:
        names = os.walk(path).next()[1]
    except AttributeError:
        names = next(os.walk(path))[1]

    names.sort()
    dir_paths = [os.path.join(path, n) for n in names]

    return names, dir_paths


def get_files(path, formats=None):
    """Get files contained in path

    Arguments:
        path {str} -- path

    Keyword Arguments:
        formats {str/list} -- file formats; if None take all (default: {None})

    Returns:
        list -- file names
        list -- file paths
    """

    if formats:

        if isinstance(formats, str):
            formats = [formats]
        else:
            assert isinstance(formats, list)

        names = []
        paths = []

        for f_format in formats:
            files = [f for f in os.listdir(path)
                     if re.match(r'.*\.{}'.format(f_format), f)]

            files.sort()
            names.extend(files)
            paths.extend([os.path.join(path, f) for f in files])

        return names, paths

    names = os.listdir(path)
    names.sort()
    paths = [os.path.join(path, f) for f in names]

    return names, paths


def write_h5(path, data):
    """Write h5 file

    Arguments:
        path {str} -- file path where to save the data
        data {seriaizable} -- data to be saved

    Raises:
        NotImplementedError -- non serializable data to save
    """

    if '.h5' not in path[-3:]:
        path += '.h5'

    hf = h5py.File(path, 'w')

    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v[0], str):
                v = [a.encode('utf8') for a in v]
            hf.create_dataset(k, data=v)
    elif isinstance(data, list):
        hf.create_dataset('val', data=data)
    elif isinstance(data, np.ndarray):
        hf.create_dataset('val', data=data)
    else:
        raise NotImplementedError
    hf.close()


def read_h5(path):
    """Load data from h5 file

    Arguments:
        path {str} -- file path

    Raises:
        FileNotFoundError -- Path not pointing to a file

    Returns:
        dict -- dictionary containing the data
    """

    if not os.path.isfile(path):
        raise FileNotFoundError()

    data_files = dict()
    h5_data = h5py.File(path)
    tags = list(h5_data.keys())
    for tag in tags:
        tag_data = np.asarray(h5_data[tag]).copy()
        data_files.update({tag: tag_data})
    h5_data.close()

    return data_files


def write_json(path, data):
    """Save data into a json file

    Arguments:
        path {str} -- path where to save the file
        data {serializable} -- data to be stored
    """

    assert isinstance(path, str)
    with open(path, 'w') as out_file:
        json.dump(data, out_file, indent=2)


def read_json(path):
    """Read data from json file

    Arguments:
        path {str} -- file path

    Returns:
        dict -- data
    """

    with open(path, 'r') as in_file:
        data = json.load(in_file)

    return data
