#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Last Change: Tue Jul 17 05:00 PM 2007 J

# The code and descriptive text is copyrighted and offered under the terms of
# the BSD License from the authors; see below. However, the actual dataset may
# have a different origin and intellectual property status. See the SOURCE and
# COPYRIGHT variables for this information.

# Copyright (c) 2007 David Cournapeau <cournape@gmail.com>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     * Neither the author nor the names of any contributors may be used
#       to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import numpy as np
from ..vtypes import integer
from ..utils import standard_properties, standard_classification_loader
__docformat__ = 'restructuredtext'

COPYRIGHT   = """This is public domain. """
name = "German Dataset"
short_name = "German Dataset"
url = 'http://www.liacc.up.pt/ML/old/statlog/datasets.html'
SOURCE      = """
http://www.liacc.up.pt/ML/old/statlog/datasets.html

Professor Dr. Hans Hofmann 
Institut für Statistik und Ökonometrie Universität Hamburg 
FB Wirtschaftswissenschaften 
Von-Melle-Park 5 
2000 Hamburg 13

Two datasets are provided. the original dataset, in the form provided by Prof.
Hofmann, contains categorical/symbolic attributes and is in the file
"german.dat".  For algorithms that need numerical attributes, Strathclyde
University produced the file "german.numer". This file has been edited and
several indicator variables added to make it suitable for algorithms which
cannot cope with categorical variables. Several attributes that are ordered
categorical (such as attribute 17) have been coded as integer. This was the
form used by StatLog. 

Here (milksets), only the numeric datasets are provided.
"""

notes = """
Number of Instances: 1000. 700 for class 0 (good credit) and 300 for class 1
(bad credit).

Number of Attributes: 24.

label: 0 for good credit, +1 for bad credit
"""
label_names = ['good_credit', 'bad_credit']
missing_values = False
value_types = [
    # FIXME
    # This is wrong! Not all outputs are integers (some are categorical),
    # but the above does not give enough information to know which features are what.
    integer('feat%s' % (i+1)) for i in xrange(24)
    ]

@standard_classification_loader(name)
def load(force_contiguous=True):
    """load the german data and returns them.
    
    :returns:
        data: dict
            Contains the following values:
                'data' : the actual data
                'label' : label[i] is the label index of data[i]
                'class' : class[label[i]] is the label name of data[i]
    """
    import numpy
    import pickle
    import gzip
    from os.path import dirname, join
    features,labels = pickle.load(gzip.GzipFile(join(dirname(__file__), 'german.pp.gz')))
    featnames = features.keys()
    featnames.sort()
    nfeatures = []
    for k in featnames:
        nfeatures.append(map(float,features[k]))
    nfeatures = np.array(nfeatures)
    features = nfeatures.T
    if force_contiguous:
        features = features.copy()
    labels = np.array([(lab == '+1') for lab in labels])
    labels = labels.astype(np.int)
    return features,labels
