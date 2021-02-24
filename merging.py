# merge the x y z values with the final_nan file
import pandas as pd
import numpy as np

df = pd.read_csv("odometry.csv")
df_2 = pd.read_csv("copy.csv")
df_2["image"] = df_2["image"].astype(int)

for i in range(len(df_2)):
    for j in range(len(df)):
        index_value_of_odometry = j
        if df_2["image"][i] == df["index"][index_value_of_odometry]:
            df_2["x_values"][i] = df["x"][index_value_of_odometry]
            df_2["y_values"][i] = df["y"][index_value_of_odometry]
            df_2["z_values"][i] = df["z"][index_value_of_odometry]

# print(df_2)
df_2.to_csv("final.csv")
# print(df.columns)