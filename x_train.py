import numpy as np
from numpy.core.fromnumeric import resize
import pandas as pd
import cv2

list_array_1 = []
list_array_2 = []
list_array_3 = []
for i in range(500):
    img = cv2.imread(f"/home/mononoke/Desktop/data/images_only/frame{i}.jpg")
    img = cv2.resize(img,(224,224))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    list_array_1.append(img)
arr_1 = np.array(list_array_1)
np.save("/home/mononoke/Desktop/data/numpy_arrays/x_1.npy",arr_1)
for i in range(500,1000,1):
    img = cv2.imread(f"/home/mononoke/Desktop/data/images_only/frame{i}.jpg")
    img = cv2.resize(img,(224,224))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    list_array_2.append(img)
for i in range(1000,1344,1):
    img = cv2.imread(f"/home/mononoke/Desktop/data/images_only/frame{i}.jpg")
    img = cv2.resize(img,(224,224))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    list_array_3.append(img)

np.set_printoptions(threshold=np.inf)

arr_2 = np.array(list_array_2)
arr_3 = np.array(list_array_3)

np.save("/home/mononoke/Desktop/data/numpy_arrays/x_2.npy",arr_2)
np.save("/home/mononoke/Desktop/data/numpy_arrays/x_3.npy",arr_3)
