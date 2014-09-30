import cPickle

import pprint
import gzip
import numpy as np


filename = '../data/mnist.pkl.gz'
targetfile = '../data/mnist_less.pkl'
f = gzip.open(filename, 'rb')

dataset = cPickle.load(f)
dataset_less = ()
# dataset = [(data[0:data.shape[0]/50], tag[0:tag.shape[0]/50]) for data, tag in dataset]
compress_rate = 50
for data, tag in dataset:
    size = data.shape[0]
    index = np.random.randint(size, size = size/compress_rate)
    set = (data[index], tag[index])
    dataset_less += (set,)

for data, tag in dataset_less:
    print data.shape, tag.shape
    print np.bincount(tag)


f = open(targetfile,'wb')
cPickle.dump(dataset_less, f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()





