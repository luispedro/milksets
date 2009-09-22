import numpy as np
MURPHYLAB_HELA2D_PATH = '/home/luispedro/work/murphylab/images/hela-2d/'
print r'''\
This is only to be run if you have got the Murphylab images installed at
    %s

Otherwise, you will get errors!
''' % MURPHYLAB_HELA2D_PATH
import pyslic
imgs = pyslic.image.io.dirtransversal.dirtransversal(MURPHYLAB_HELA2D_PATH)
labels = np.array([img.label for img in imgs])
features = pyslic.computefeatures(imgs, 'SLF7DNA')
np.savez('murphylab.npz', features=features, labels=labels)
