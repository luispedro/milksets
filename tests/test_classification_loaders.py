import milksets.wine
import milksets.yeast

def test_classification_loaders():
    def test_loader(loader):
        features,labels = loader()
        assert len(features) == len(labels)
        assert labels.min() == 0
        assert (features.std(0)**2).sum() > 1e-8
    yield test_loader, milksets.wine.load
    yield test_loader, milksets.yeast.load

