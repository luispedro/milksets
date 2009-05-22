import milksets.census
def test_census():
    features,labels = milksets.census.load()
    assert len(features) == len(labels)
    assert labels.min() == 0
    assert labels.max() == len(milksets.census.label_names) - 1
