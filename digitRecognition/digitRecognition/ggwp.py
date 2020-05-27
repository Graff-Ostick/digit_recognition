from PIL import Image, ImageDraw
from resizeimage import resizeimage
from sklearn import datasets
from sklearn.svm import SVC
from scipy import misc
import numpy as np
import imageio
import imutils

len_array =  3
list = []
wr_file = open("numbers.txt", "w")

digits = datasets.load_digits()
features = digits.data
labels = digits.target

slf = SVC(gamma = 0.001)
slf.fit(features, labels)

print(features.shape)

#print(slf.predict([features[-2]]))
for i in range(len_array):
    img = "8"+str(i)+".jpg"

    img = imageio.imread(img)
    img = misc.imresize(img, (8,8))
    img = img.astype(digits.images.dtype)
    img = misc.bytescale(img, high =16, low = 0)

    x_test = []

    for eachRow in img:
        for eachPixel in eachRow:
            x_test.append(sum(eachPixel)/3.0)
    print("------------------------------")
    print("----your ansver hear----------")

    print(slf.predict([x_test]))
    number = str(slf.predict([x_test]))

    #list = list.append(number[0])
    wr_file.write(number[1])
    i+=1

wr_file.close("numbers.txt")
