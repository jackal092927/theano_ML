import cPickle

import pprint
import gzip
from numpy  import *

filename = '../data/mnist.pkl.gz'
targetfile = '../data/mnist_less.pkl'
f = gzip.open(filename, 'rb')
# train_set, valid_set, test_set = pickle.load(f)
#
# t_input, t_output = train_set
# v_input, v_output = valid_set
# test_input, test_output = test_set

dataset = cPickle.load(f)
print type(dataset)
dataset = [(data[0:data.shape[0]/50], tag[0:tag.shape[0]/50]) for data, tag in dataset]
# :
#     data_size = data.shape[0] / 50
#     data = data[0:data_size]
#     tag_size = tag.shape[0] / 50
#     tag = tag[0:tag_size]
#     dataset[1] = (data, tag)


print type(dataset)
train_set, valid_set, test_set = dataset
t_input, t_output = train_set
v_input, v_output = valid_set
test_input, test_output = test_set

f = open(targetfile,'wb')
cPickle.dump(dataset, f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()


print t_input.shape

print v_input.shape

print test_input.shape



