# -*- coding: utf-8 -*-
# Copyright (C) 2012-2014, Luis Pedro Coelho <luis@luispedro.org>
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


import numpy as np
from os.path import dirname
from ..vtypes import continuous
from ..utils import standard_properties, standard_classification_loader

__all__ = ['load'] + standard_properties

name = 'iris'
short_name = 'Iris'
long_name = 'Iris Flower Data Set'
reference = '''\
Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual
Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to Mathematical
Statistics" (John Wiley, NY, 1950). 
'''
url = 'http://archive.ics.uci.edu/ml/datasets/Iris'
data_source = 'UCI'
label_names = ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica']

missing_values = False
value_types = [
    continuous('sepal_length'),
    continuous('sepal_width'),
    continuous('petal_length'),
    continuous('petal_width'),
    ]

@standard_classification_loader(name)
def load(force_contiguous=True):
    from bz2 import BZ2File
    base = dirname(__file__) + '/data/'
    features = []
    labels = []
    low_label_names = [ell.lower() for ell in label_names]
    for line in BZ2File(base+'correct.data.bz2'):
        line = line.decode('utf-8')
        tokens = line.strip().split(',')
        if len(tokens) < 4:
            break
        features.append(np.array(list(map(float, tokens[:4]))))
        name = tokens[4]
        name = name.lower()
        name = name.replace('-', ' ')
        # The original names are in British English:
        name = name.replace('color', 'colour')
        labels.append(low_label_names.index(name))
    labels = np.array(labels)
    features = np.array(features)
    return features, labels


