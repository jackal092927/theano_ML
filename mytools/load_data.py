from scipy import misc
from numpy import *
import matplotlib.pyplot as plt
import cPickle
import gzip


#dataset = './data/mnist.pkl.gz'
dataset = '../data/mydata.pkl'
f = open(dataset, 'rb')
#train_set, valid_set, test_set = cPickle.load(f)
set_list = cPickle.load(f)
f.close()

for set in set_list:
    data, tag = set
    print data.shape, tag.shape

