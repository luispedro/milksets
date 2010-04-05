# -*- coding: utf-8 -*-
# Copyright (C) 2009-2010, Luis Pedro Coelho <lpc@cmu.edu>
# Software Distributed under the MIT License
from __future__ import division, with_statement
import numpy as np
from .vtypes import *

def category2index(features, types):
    '''
    transformed = category2index(features, types)

    Transforms the dataset by replacing all categorical elements
    by an index.

    Missing values (i.e., '' entries) get replaced by -1
    
    Inputs
    -------
        * features: features vector
        * types: a sequence of vtypes
    '''
    def storage_type(types):
        res = bool
        for t in types:
            if isinstance(t,continuous):
                return float
            if not isinstance(t,boolean):
                res = int
        return res

    output = np.empty(features.shape, dtype=storage_type(types))
    for i,f in enumerate(features):
        for j,t,val in zip(xrange(len(f)),types, f):
            if isinstance(t, categorical):
                output[i,j] = (t.categories.index(val) if val else -1)
            else:
                output[i,j] = val
    return output

def category2boolarray(features, types):
    '''
    transformed = category2index(features, types)

    Transforms the dataset by replacing all categorical elements
    by a set of boolean entries corresponding, so that, in each 
    instance, only one of the boolean entries is set to true.

    Missing values (i.e., '' entries) are handled naturally (no
    bit is set to one).
    
    Inputs
    -------
        * features: features vector
        * types: a sequence of vtypes
    '''
    def storage_type(types):
        res = bool
        for t in types:
            if isinstance(t,continuous):
                return float
            if not isinstance(t,boolean) and not isinstance(t,categorical):
                res = int
        return res
    def _lenfor(t):
        if isinstance(t,categorical):
            return len(t.categories)
        return 1
    nlen = sum(_lenfor(t) for t in types)
    output = np.empty((len(features),nlen),storage_type(types))
    for i,f in enumerate(features):
        j = 0
        for t,val in zip(types, f):
            if isinstance(t, categorical):
                if val:
                   output[i,j+t.categories.index(val)] = 1
                j += len(t.categories)
            else:
                output[i,j] = val
                j += 1
    return output

# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
