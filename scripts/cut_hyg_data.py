##
import numpy as np
import pandas as pd

df = pd.read_csv("hygdata_v3.csv")

columns_to_keep = ['id', 'ra', 'dec', 'proper', 'x', 'y', 'z']
all_stars = df[columns_to_keep]
named_stars = all_stars[all_stars['proper'].notnull()]

print(all_stars.info())

all_stars.to_csv("hygdata_id_proper_xyz.csv", index=False, float_format='%.6f')
named_stars.to_csv("hygdata_id_proper_xyz_only_named_stars.csv", index=False, float_format='%.6f')
##