import matplotlib.image as image
import os
import pandas as pd
import cv2
from tqdm import tqdm
import numpy as np
from PIL import Image
path = "Faces/"
filename = 'faces.csv'
files = os.listdir(path)
print(files)
dim = (100, 100)
df = pd.DataFrame(columns = [f'pix-{i}' for i in range(1, 1+(dim[0]*dim[1]))]+['class'])
count = 1
for j in range(0,len(files)):
    if files[j] == ".DS_Store":
        continue
    path2 = "Faces/"+files[j]+"/"
    print(path2)
    files2 = os.listdir(path2)
    print(files2)
    cls = j
    prev = 1
    for i in tqdm(range(1, 1+len(files2))):
        if files2[i-1] == ".DS_Store":
            continue
        img =Image.open(path2+files2[i-1])
        for k in range(1):
            df.loc[count] = list(img.getdata()) + [cls]
            count += 1
        prev = prev + len(files2)+1

df.to_csv(filename,index = False)
print('Task Completed')


#%%
