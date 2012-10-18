#!/usr/bin/env bash

wget http://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data
wget http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
wget http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names
mv bezdekIris.data correct.data
mv iris.data uci_mistake.data

bzip2 correct.data
bzip2 uci_mistake.data

