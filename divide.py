import pandas as pd
import numpy as np
df = pd.read_csv("final_output_merging.csv")
# divide it into the number of grids S = 14 (14*14 grids)

grids = 7 
# first we need to get the grids and then we are going to make things happen.

# first we have to resize the image of it and then proceed.
width = 224
height = 224
width_image = 1280
height_image = 720

df["x_center"] = df["x_center"]*width//width_image
df["y_center"] = df["y_center"]*height//height_image
df["width"] = df["width"]*width//width_image
df["height"] = df["height"]*height//height_image
df["xmin"] = df["xmin"]*width//width_image
df["ymin"] = df["ymin"]*height//height_image
df["xmax"] = df["xmax"]*width//width_image
df["ymax"] = df["ymax"]*height//height_image

df.to_csv(f"to_specific_image{width}_{height}.csv")

# now we have to divide into grids 
grids_div = width/grids
df["x_center"] = round(df["x_center"]/grids_div,2)
df["y_center"] = round(df["y_center"]/grids_div,2)
df["width"] = round(df["width"]/grids_div,2)
df["height"] = round(df["height"]/grids_div,2)
df["xmin"] = round(df["xmin"]/grids_div,2)
df["ymin"] = round(df["ymin"]/grids_div,2)
df["xmax"] = round(df["xmax"]/grids_div,2)
df["ymax"] = round(df["ymax"]/grids_div,2)
df.to_csv("grids_7.csv")

# always remember that they start from 0
df = pd.read_csv("grids_7.csv")
# Now we want to find in which they are and how are they doing...
a = np.floor(df["xmin"])
b = np.floor(df["ymin"])
c = np.floor(df["xmax"])
d = np.floor(df["ymax"])
e = np.floor(df["x_center"])
f = np.floor(df["y_center"])
# g = np.floor(df["height"])
# h = np.floor(df["width"])
# for height and width we just have to divide it by 19 
df["x_center"] -= e
df["y_center"] -= f
# df["width"] = 
# df["height"] = 
df["xmin"] -= a
df["ymin"] -= b
df["xmax"] -= c
df["ymax"] -= d

df.to_csv("grids_final_7.csv")
