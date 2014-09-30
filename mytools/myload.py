from PIL import Image
import gzip
from os import listdir

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import cPickle

import gzip

# img = Image.open('./data/test1.png').convert('LA')
# img.save('./data/test1gray.png')

mysize = 28,28
srcPath = '/Volumes/MY PASSPORT/work/toXinCheng/'
dirname = ('negative/', 'CIN1/', 'CIN2/', 'CIN3/')


valiSize = 50
testSize = 50

trainImgList = []
trainTagList = np.array([])
validateImgList = []
validateTagList = np.array([])
testImgList = []
testTagList = np.array([])

for i, d in enumerate(dirname):

    tPath = srcPath + d + 'small/'

    for j,f in enumerate(listdir(tPath)):
        img = misc.imread(tPath + f, 1)
        img = img.reshape(1, 28*28)

        if j < valiSize:
            validateImgList.append(img)
            validateTagList = np.append(validateTagList, i)
        elif j < testSize + valiSize:
            testImgList.append(img)
            testTagList = np.append(testTagList, i)
        else:
            trainImgList.append(img)
            trainTagList = np.append(trainTagList, i)


data = np.vstack(validateImgList)
#tag = np.vstack(validateTagList)
tag = validateTagList
print data.shape, tag.shape
validateSet = (data, tag)

data = np.vstack(testImgList)
#tag = np.vstack(testTagList)
tag = testTagList
testSet = (data, tag)
print data.shape, tag.shape

data = np.vstack(trainImgList)
#tag = np.vstack(trainTagList)
tag = trainTagList
trainSet = (data, tag)
print data.shape, tag.shape
print ""

data = (trainSet, trainSet, testSet)
f = file('./data/mydata_small.pkl','wb')
cPickle.dump(data, f, protocol=cPickle.HIGHEST_PROTOCOL)
f.close()

# img = misc.imread('./data/test1small.png', 1)
# print type(img)

# img = img.reshape(1,2)
# imgList = []

# for i in range(2000):
#     imgList.append(img)

# img = vstack(imgList)

# tag = zeros((2000))
# print tag.shape, type(tag)

# data = (img, tag)
# data = (data, data ,data)

# f = file('./data/mydata.pkl','wb')
# cPickle.dump(data, f, protocol=cPickle.HIGHEST_PROTOCOL)
# f.close()

# dataset = './data/mydata.pkl'
# f = file(dataset, 'rb')
# train_set, train_set2, train_set3 = cPickle.load(f)
# img, tag = train_set
# print img.shape, tag.shape
# img, tag = train_set2
# print img.shape, tag.shape
# img, tag = train_set3
# print img.shape, tag.shape
