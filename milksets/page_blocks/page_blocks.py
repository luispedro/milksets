# -*- coding: utf-8 -*-
# Copyright (C) 2012, Luis Pedro Coelho <luis@luispedro.org>
# Software Distributed under the MIT License


from __future__ import division
from os.path import dirname
from ..utils import standard_properties, standard_classification_loader
from ..vtypes import *

__all__ = ['load'] + standard_properties

name = 'Page Blocks'
short_name = 'page-blocks'
long_name = 'UCI Blocks Classification'
reference = '''\
"A Further Comparison of Simplification Methods for Decision-Tree Induction."
In D. Fisher and H. Lenz (Eds.), "Learning  from Data: Artificial Intelligence
and Statistics V", Lecture Notes in Statistics, Springer Verlag, Berlin, 1995.
'''
url = 'http://archive.ics.uci.edu/ml/datasets/Page+Blocks+Classification'
data_source = 'UCI'
value_types = [
    
    integer('height'),      # Height of the block.
    integer('lenght'),      # Length of the block. 
    integer('area'),        # Area of the block (height * lenght);
    continuous('eccen'),    # Eccentricity of the block (lenght / height);
    continuous('p_black'),  # Percentage of black pixels within the block (blackpix / area);
    continuous('p_and'),    # Percentage of black pixels after the application of the Run Length Smoothing Algorithm (RLSA) (blackand / area);
    continuous('mean_tr'),  # Mean number of white-black transitions (blackpix / wb_trans);
    integer('blackpix'),    # Total number of black pixels in the original bitmap of the block.
    integer('blackand'),    # Total number of black pixels in the bitmap of the block after the RLSA.
    integer('wb_trans'),    # Number of white-black transitions in the original bitmap of the block.

    ]	
label_names = ['text', 'hline', 'graphic', 'vline', 'picture']
missing_values = False

_datafile = dirname(__file__)+'/data/page-blocks.data.gz'

@standard_classification_loader(name)
def load(force_contiguous=True):
    import gzip
    import numpy as np
    data = np.loadtxt(gzip.open(_datafile))
    features = data[:,:-1]
    labels = data[:,-1]
    labels -= 1
    if force_contiguous:
        features = features.copy()
        labels = labels.copy()
    return features,labels


