import milksets.scene
def test_scene():
    features, labels = milksets.scene.load()
    assert len(features) == len(labels)
