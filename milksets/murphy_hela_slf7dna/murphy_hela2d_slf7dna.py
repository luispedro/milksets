# -*- coding: utf-8 -*-
# Copyright (C) 2009-2010, Luis Pedro Coelho <lpc@cmu.edu>
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

name = 'Murphy Lab 2D HeLa (SLF7DNA)'
short_name = 'Hela2D'
long_name = name
reference = '''\
'''
url = 'http://murphylab.cbi.cmu.edu/download'
data_source = 'MurphyLab'
label_names = ['dap', 'erdak', 'giant', 'gpp130', 'h4b4', 'mc151', 'nucle', 'phal', 'tfr', 'tubul']
missing_values = False
value_types = [
    continuous('_%s' % i) for i in xrange(90)
    ]

_datafile = dirname(__file__)+'/data/murphylab.npz'

@standard_classification_loader(name)
def load(force_contiguous=True):
    data = np.load(_datafile)
    features = data['features']
    labels = np.array([label_names.index(lab) for lab in data['labels']])
    if force_contiguous:
        features = np.ascontiguousarray(features)
        labels = np.ascontiguousarray(labels)
    return features,labels

# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
