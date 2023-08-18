import os

data_dir = 'cars/train'

folders = os.listdir(data_dir)

with open('labels.txt', "w") as f:
    for folder in folders:
        f.write(folder + '\n')
