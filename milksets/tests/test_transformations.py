import milksets.abalone
import milksets.transformations
import numpy as np
features,labels = milksets.abalone.load()
sex = milksets.abalone.value_types[0].categories

def test_category2boolarray():
    orig = features[:,0]
    boolarray = milksets.transformations.category2boolarray(features,milksets.abalone.value_types)[:,:3]
    assert np.all( (orig == sex[0]) == (boolarray[:,0] == 1) )
    assert np.all( (orig == sex[1]) == (boolarray[:,1] == 1) )
    assert np.all( (orig == sex[2]) == (boolarray[:,2] == 1) )

def test_category2index():
    orig = features[:,0]
    indexed = milksets.transformations.category2index(features,milksets.abalone.value_types)[:,0]
    assert np.all( (orig == sex[0]) == (indexed == 0) )
    assert np.all( (orig == sex[1]) == (indexed == 1) )
    assert np.all( (orig == sex[2]) == (indexed == 2) )

