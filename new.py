# extract all the images from data 1 and put them into other file

import os
import shutil
for i in range(1345):
    shutil.move(f'/home/mononoke/Desktop/data/data_1/frame{i}.jpg',"/home/mononoke/Desktop/data/images_only")