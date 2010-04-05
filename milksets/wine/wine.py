# -*- coding: utf-8 -*-
# Copyright (C) 2008-2010, Luis Pedro Coelho <lpc@cmu.edu>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

from __future__ import division
import numpy as np
from os.path import dirname
from ..vtypes import continuous
from ..utils import standard_properties, standard_classification_loader

__all__ = ['load'] + standard_properties

name = 'Wine'
short_name = 'Wine'
long_name = 'UCI Wine'
reference = '''\
Forina, M. et al, PARVUS -
An Extendible Package for Data Exploration, Classification and Correlation.
Institute of Pharmaceutical and Food Analysis and Technologies, Via Brigata Salerno,
16147 Genoa, Italy.
'''
url = 'http://archive.ics.uci.edu/ml/datasets/Wine'
data_source = 'UCI'
label_names = [1,2,3]
missing_values = False
value_types = [
    continuous('_%s' % i) for i in xrange(13)
    ]

_winedatafile = dirname(__file__)+'/data/wine.data'

@standard_classification_loader(name)
def load(force_contiguous=True):
    data  = np.array([map(float,line.split(',')) for line in file(_winedatafile)])
    labels = data[:,0] - 1 # Wine dataset is 1..3
    features = data[:,1:]
    if force_contiguous:
        labels = labels.copy()
        features = features.copy()
    return features,labels


