import Image
from scipy import misc
from numpy import *
import matplotlib.pyplot as plt
import cPickle
import gzip


dataset = './data/mnist.pkl.gz'
f = gzip.open(dataset, 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()

myInput, tag = train_set

print myInput.shape
print tag.shape
