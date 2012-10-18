from milksets.iris import load

def test_iris():
    features, labels = load()
    assert len(labels) == 150
    assert len(features) == 150
    assert features.shape == (150,4)

