import pandas as pd
import xml.etree.ElementTree as Xet
import numpy as np
cols = ["image","xmin","ymin","xmax","ymax"]
rows = [] 
df = pd.DataFrame(columns=cols)
# Parsing the XML file 
list = []
for number in range(1345):
    try:
        xmlparse = Xet.parse(f'/home/mononoke/Desktop/data/xml/frame{number}.xml') 
        root = xmlparse.getroot() 
        for child in root:
            # print(child)
            if child.tag == "object":
                for x in child:
                    if x.tag == "bndbox":
                        xmin = []
                        xmin.append(int(f'{number}')) # the number of the image 
                        for y in x:
                            if (y.tag=="xmin"):
                                xmin.append(int(y.text))
                            elif (y.tag=="xmax"):
                                xmin.append(int(y.text))
                            elif (y.tag=="ymin"):
                                xmin.append(int(y.text))
                            else:
                                xmin.append(int(y.text))
                            # now we have to append this in the columns of the dataframe
                        df.loc[len(df)] = xmin
    except FileNotFoundError:
        # df.loc[len(df)] = [int(f'{number}'),np.nan,np.nan,np.nan,np.nan]
        print("hello")
df.to_csv("final.csv")
print(len(list))