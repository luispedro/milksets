# -*- coding: utf-8 -*-
# Copyright (C) 2012, Luis Pedro Coelho <luis@luispedro.org>
# Software Distributed under the MIT License

def run():
    import nose
    from os import path
    currentdir = path.dirname(__file__)
    updir = path.join(currentdir, '..')
    nose.run('milk', argv=['', '--exe', '-w', updir])


