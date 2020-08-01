from PIL import Image
import numpy as np
from pprint import pprint
from matplotlib import pyplot as plt
import os
import pickle
import pandas as pd


def get_data(num):
    a = os.listdir(f"trainingSet\\{num}")
    im_list = []
    for i in range(len(a)):
        image = Image.open(f"F:\\Data Science\\Learning and Testing\\im_data\\trainingSet\\trainingSet\\{num}\\{a[i]}")
        im = np.asarray(image)
        im = im.flatten()
        im_list.append(im)
    return [num,im_list]
def dump_data(fname,data):
    with open(fname, "wb") as f:
        pickle.dump(data,f)
data_list = []
for i in range(0,10):
    print("getting data for",i)
    data_list.append(get_data(f"{i}"))
dump_data("images.bin",data_list)
data = get_data(0)
#print(data[0][0])
# plt.imshow(data[0][0].reshape(28,28))
# plt.show()








