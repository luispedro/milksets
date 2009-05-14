import milksets.wine
def test_wine():
    features,labels = milksets.wine.load()
    assert len(features) == len(labels)

