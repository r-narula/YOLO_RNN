import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import os
import os

number_images = 1344
df = pd.read_csv("grids_16.csv")
df_2 = pd.read_csv("grids_final_16.csv")
number = int(np.ceil(224/7))

list_object = []
for i in range(len(df)):
    x = (i,df["image_number"][i],(int(np.floor(df["y_center"][i])),int(np.floor(df["x_center"][i])))) # which row and column does the object is in
    list_object.append(x)
# print(list_object)


list_columns = list(df.columns)
array =  np.zeros((1344,16,16,8))

images_that_have_objects = []
for i in range(len(df)):
    if df["x_center"][i] !=0 and df["y_center"][i] != 0:
        if df["image_number"][i] not in images_that_have_objects:
            images_that_have_objects.append(df["image_number"][i])

def contains_object(image_number):
    number_objects = 0
    data_object = []
    for i in list_object:
        if i[1] == image_number:
            number_objects += 1
            data_object.append(i)
    return data_object,number_objects

# os.mkdir("y_train_visualize")
for image in range(number_images):
    # see if this image contains object or not
# image = 0
    data,number=contains_object(image)
    if contains_object(image)[1]>0:
        # now if this image contains the object 
        # we need to find the grid (row*column) where there is obj center
        for center in data:
            # center[2] gives us the object center
            y = center[2][1]
            x = center[2][0]
            row_number = center[0]
            # we have to take the values from the table 
            array[image][y][x] = [np.round(1,0),round(df_2["x_center"][row_number],2),round(df_2["y_center"][row_number],2),round(df_2["width"][row_number],2),round(df_2["height"][row_number],2),round(df_2["x_values_odo"][row_number],2),round(df_2["y_values_odo"][row_number],2),round(df_2["z_values_odo"][row_number],2)]
    content = str(array[image])
    # f = open(f"y_train_visualize/{image}.txt","w")
    # f.write(content)
    # f.close()
np.set_printoptions(threshold=np.inf)
np.save("/home/mononoke/Desktop/data/numpy_arrays/y_train_16.npy",array)
# print(array.shape)