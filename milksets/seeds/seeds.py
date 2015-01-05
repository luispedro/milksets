# -*- coding: utf-8 -*-
# Copyright (C) 2012, Luis Pedro Coelho <luis@luispedro.org>
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

name = 'seeds'
short_name = 'Seeds'
long_name = 'Seeds Flower Data Set'
reference = '''\
M. Charytanowicz, J. Niewczas, P. Kulczycki, P.A. Kowalski, S. Lukasik, S. Zak,
'A Complete Gradient Clustering Algorithm for Features Analysis of X-ray
Images', in: Information Technologies in Biomedicine, Ewa Pietka, Jacek Kawa
(eds.), Springer-Verlag, Berlin-Heidelberg, 2010, pp. 15-24.
'''
url = 'http://archive.ics.uci.edu/ml/datasets/seeds'
data_source = 'UCI'
label_names = ['Kama', 'Rosa', 'Canadian']

missing_values = False
value_types = [
    continuous('area'), 
    continuous('perimeter'),
    continuous('compactness'),
    continuous('length of kernel'),
    continuous('width of kernel'),
    continuous('asymmetry coefficien'),
    continuous('length of kernel groove'),
    ]

@standard_classification_loader(name)
def load(force_contiguous=True):
    from bz2 import BZ2File
    base = dirname(__file__) + '/data/'
    data = np.loadtxt(base+'seeds_dataset.txt.gz')
    features = data[:,:-1]
    labels = data[:,-1]
    labels -= 1
    labels = labels.astype(int)
    if force_contiguous:
        features = features.copy()
        labels = labels.copy()
    return features, labels

