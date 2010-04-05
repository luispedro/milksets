# -*- coding: utf-8 -*-
# Copyright (C) 2009-2010, Luis Pedro Coelho <lpc@cmu.edu>
# Software Distributed under the MIT License

from __future__ import division
import numpy as np
from os.path import dirname
import gzip
from ..vtypes import *
from ..utils import standard_properties, standard_classification_loader

__all__ = ['load'] + standard_properties

name = 'Yeast'
short_name = 'Yeast'
long_name = 'UCI Yeast Subcellular Localization Dataset'
reference = '''\
Paul Horton & Kenta Nakai,
"A Probablistic Classification System for Predicting the Cellular Localization Sites of Proteins",
Intelligent Systems in Molecular Biology, 109-115.
St. Louis, USA 1996.
'''
url = 'http://archive.ics.uci.edu/ml/datasets/Yeast'
data_source = 'UCI'
label_names = ['CYT', 'ERL', 'EXC', 'ME1', 'ME2', 'ME3', 'MIT', 'NUC', 'POX', 'VAC']
value_types = [
    continuous('_%s' % i) for i in xrange(8)
    ]
missing_values = False

_datafile = dirname(__file__)+'/data/yeast.data.gz'

@standard_classification_loader(name)
def load(force_contiguous=True):
    data  = [line.split() for line in gzip.GzipFile(_datafile)]
    labels = np.array([label_names.index(items[-1]) for items in data])
    features = np.array([map(float,items[1:-1]) for items in data])
    # Arrays are continuous as is, so no need
    # to copy them, independently of the value of force_contiguous
    return features,labels


