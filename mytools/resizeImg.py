from os import listdir
from os.path import exists, isdir
from PIL import Image

mysize = 28,28
srcPath = '/Volumes/MY PASSPORT/work/toXinCheng/'
dirname = 'negative'
tPath = srcPath + dirname

for f in listdir(tPath + '/png'):
    filepath = tPath + '/png/' + f
    if isdir(filepath):
        continue

    img = Image.open(filepath).convert('LA')
    filepath = tPath + '/small/' + f
    img = img.resize(mysize, Image.ANTIALIAS)
    img.save(filepath, 'PNG')
    #print filepath
