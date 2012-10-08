#!/usr/bin/env bash

cd data
wget http://archive.ics.uci.edu/ml/machine-learning-databases/page-blocks/page-blocks.data.Z
wget http://archive.ics.uci.edu/ml/machine-learning-databases/page-blocks/page-blocks.names
uncompress page-blocks.data.Z
gzip page-blocks.data
