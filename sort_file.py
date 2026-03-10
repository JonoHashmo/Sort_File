import random
import pandas as pd
from glob import glob
import os
import shutil


### Prompt for path to csv file with correct image names###
while True:
    f_path = input("Enter path for your .csv file: ")
    try:
        foods_csv = pd.read_csv(f_path)
        break
    except:
        print("Wrong file path for HF_LF_60.csv")
        continue

### Prompt for path to stimuli folder###
while True:
    i_path = input("""Enter path for stimuli folder. (HINT: don't forget the / at the end):
    """)
    images=glob(i_path+"*.jpg")
    if not images:
        print("Wrong file path for stimuli foder. did you forget the / at the end?")
        continue
    else:
        break

###Create a list of all image names in stimuli folder###
img_names = []
for x in images:
    img_names.append(x.split('stimuli/')[-1])

###Fine names that are in both###
both=[]
for x in foods_csv["food"]:
    if x in img_names:
        both.append(x)

###Create a new Folder in your chosen path. Prompt for name and path###
while True:
    fol_path = input("""Enter the path for the location you want the new folder to be in (HINT: Dont forget to add a / at the end):
    """)
    if not os.path.exists(fol_path):
        print("Invalid path name, try again.")
        continue
    fol_name = input("Enter new folder name: ")
    full_fol_path = os.path.join(fol_path, fol_name)
    break

os.makedirs(full_fol_path)

###Copy images that appear in both###
for x in both:
    shutil.copy(i_path + x, full_fol_path)

###check for duplicate images###
seen = []
for x in both:
    if x in seen:
        print(f"Duplicate:{x}")
    seen.append(x)


print(f"""
Done!

All images existing in both files have been moved to a new file called: {fol_name}.

It's path is: {fol_path}.
""")
