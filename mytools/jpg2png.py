from os import listdir
from os.path import isdir, join, splitext
from PIL import Image

srcPath = '/Volumes/MY PASSPORT/work/toXinCheng/'
dirname = 'negative'
tPath = srcPath + dirname
for f in listdir(tPath):
    filepath = tPath + '/' + f
    if isdir(filepath):
        continue

    img = Image.open(filepath)
    filepath = tPath + '/png'
    filename = splitext(f)[0]
    filepath = filepath + '/' + filename + '.png'
    img.save(filepath, 'PNG')
