# -*- coding: utf-8 -*-
# Copyright (C) 2009-2010, Luis Pedro Coelho <lpc@cmu.edu>
# Software Distributed under the MIT License
from __future__ import division
import numpy as np
import gzip
from os.path import dirname
from ..utils import standard_properties, standard_classification_loader
from ..vtypes import *

__all__ = ['load'] + standard_properties

name = 'Abalone'
short_name = 'Abalone'
long_name = 'UCI Abalone'
reference = '''\
Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994) 
"The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait", 
Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288)
'''
url = 'http://archive.ics.uci.edu/ml/datasets/Abalone'
data_source = 'UCI'
value_types = [
	categorical('Sex',['M','F','I']), # I is for "Infant"
	continuous('Length'),
	continuous('Diameter'),
	continuous('Height'),
	continuous('Whole Weight'),
	continuous('Shucked Weight'),
	continuous('Viscera Weight'),
	continuous('Shell Weight'),
    ]	
label_names = continuous('Rings')
missing_values = False

_datafile = dirname(__file__)+'/data/abalone.data.gz'

@standard_classification_loader(name)
def load(force_contiguous=True):
    features = []
    labels = []
    for line in gzip.GzipFile(_datafile):
        items = line.split(',')
        features.append(items[:-1])
        labels.append(int(items[-1].strip()))
    features = np.array(features)
    labels = np.array(labels)
    return features,labels


