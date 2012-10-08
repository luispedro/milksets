import milksets.abalone
def test_abalone():
    features,labels = milksets.abalone.load()
    assert len(features) == len(labels)
