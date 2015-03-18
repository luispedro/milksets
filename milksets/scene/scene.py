# -*- coding: utf-8 -*-
# Copyright (C) 2011, Luis Pedro Coelho <luis@luispedro.org>
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
import bz2

__all__ = ['load'] + standard_properties

name = 'scene'
short_name = 'Scene'
long_name = 'Scene Classification'
reference = '''\
Matthew R. Boutell, Jiebo Luo, Xipeng Shen, and Christopher M. Brown. Learning
multi-label scene classification. Pattern Recognition, 37(9):1757-1771, 2004
'''
url = 'http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multilabel.html'
data_source = 'LibSVM'
label_names = [i for i in range(6)]
missing_values = False
value_types = [
    continuous('_{}'.format(i)) for i in range(294)
    ]

@standard_classification_loader(name)
def load(force_contiguous=True):
    base = dirname(__file__) + '/data/'
    Tr_f, Tr_l = _load_file(base+'scene_train.bz2')
    Te_f, Te_l = _load_file(base+'scene_test.bz2')
    features = np.concatenate( (Tr_f,Te_f) )
    Tr_l.extend(Te_l)
    return features, Tr_l



def _load_file(fname):
    labels = []
    features = []
    for line in bz2.BZ2File(fname):
        tokens = line.strip().split(b' ')
        labels.append([int(t) for t in tokens[0].split(b',')])
        cur = np.zeros(294, float)
        for i,tok in enumerate(tokens[1:]):
            index,val = tok.split(b':')
            assert int(index) == (i+1)
            cur[i] = val
        features.append(cur)
    return np.array(features), labels


