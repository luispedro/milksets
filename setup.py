# -*- coding: utf-8 -*-
# Copyright (C) 2009-2012, Luis Pedro Coelho <luis@luispedro.org>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
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
    print('''
setuptools not found.

On linux, the package is often called python-setuptools''')
    from sys import exit
    exit(1)
exec(compile(open('milksets/milksets_version.py').read(),
             'milksets/milksets_version.py', 'exec'))


packages = find_packages()
if 'tests' in packages: packages.remove('tests')
datasets = [
    'wine',
    'murphy_hela_slf7dna',
    'yeast',
    'german',
    'iris',
    'seeds',
    'page_blocks',
    ]

package_dir = dict([
    ('milksets.{0}'.format(d),'milksets/{0}'.format(d))
        for d in datasets])
package_data =  dict([
    ('milksets.{0}'.format(d),['data/*'])
        for d in datasets])

setup(name = 'milksets',
      version = __version__,
      description = 'Milk sets: Machine Learning Datasets',
      author = 'Luis Pedro Coelho',
      author_email = 'luis@luispedro.org',
      url = 'http://luispedro.org/software/milksets/',
      packages = packages,
      package_dir = package_dir,
      package_data = package_data,
      test_suite = 'nose.collector',
      )


