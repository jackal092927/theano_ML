__author__ = 'Jackal'

import scipy.io
import gzip
from os import listdir, path
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import cPickle

import numpy as np

# dirpath = '../data/850invariPLBP+1008PLAB-79.93/ftr/'
# filename_list = ['negativeFeatures', 'CIN1Features', 'CIN2Features', 'CIN3Features', 'cancerFeatures']
# targetfile = '../data/feature.pkl'
dirpath = '../data/850invariPLBP-78.84/'
filename_list = ['Neg', 'Pos']
targetfile = '../data/feature850-2.pkl'

filetype = '.mat'
filelist = [dirpath + filename + filetype for filename in filename_list]
mat_list = [scipy.io.loadmat(file) for file in filelist if path.isfile(file)]
data_list = [mat[file] for mat, file in zip(mat_list, filename_list)]


validat_list = []
valitag_list = []
testdat_list = []
testtag_list = []
trandat_list = []
trantag_list = []

for i, data in enumerate(data_list):
    size = data.shape[0] / 100 *10
    valitag_list += [i]*size
    testtag_list += [i]*size
    trantag_list += [i]*(data.shape[0] - (2*size))
    validat_list.append(data[0:size, :])
    testdat_list.append(data[size: 2*size, :])
    trandat_list.append(data[2*size: data.shape[0], :])



trandat_list = np.vstack(trandat_list)
transet = (np.vstack(trandat_list), np.array(trantag_list))
valiset = (np.vstack(validat_list), np.array(valitag_list))
testset = (np.vstack(testdat_list), np.array(testtag_list))

data = (transet, valiset, testset)

print [(dat.shape, tag.shape) for (dat, tag) in data]

f = open(targetfile,'wb')
cPickle.dump(data, f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()


# pos_file = './data/850invariPLBP-78.84/Pos.mat'
# neg_file = './data/850invariPLBP-78.84/Neg.mat'

# f = h5py.File(pos_file,'r')
# data = f.get('data/variable1')
# data = np.array(data) # For converting to numpy array
# print data


#mat = scipy.io.loadmat(cin1_mat)
#print mat['CIN1Features']

#pos_dat = mat['Pos']
#trainSet = pos_dat[0:100, :]
#print trainSet.shape



# data = (trainSet, validateSet, testSet)
# f = file('./data/feature.pkl','wb')
# cPickle.dump(data, f, protocol=cPickle.HIGHEST_PROTOCOL)
# f.close()


#print mat

