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
try:
    from setuptools import *
except:
    print '''
setuptools not found.

On linux, the package is often called python-setuptools'''
    from sys import exit
    exit(1)


packages = find_packages()
if 'tests' in packages: packages.remove('tests')
package_dir = {
    'milksets.wine': 'milksets/wine',
    'milksets.murphy_hela_slf7dna': 'milksets/murphy_hela_slf7dna',
    'milksets.yeast': 'milksets/yeast',
    }
package_data = {
    'milksets.wine': ['data/wine.*'],
    'milksets.murphy_hela_slf7dna' : ['data/murphylab.*'],
    'milksets.yeast' : ['data/yeast.*'],
    }

setup(name = 'milksets',
      version = '0.1',
      description = 'Milk sets: Machine Learning Datasets',
      author = 'Luis Pedro Coelho',
      author_email = 'lpc@cmu.edu',
      url = 'http://luispedro.org/software/milksets/',
      packages = packages,
      package_dir = package_dir,
      package_data = package_data,
      )


# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
