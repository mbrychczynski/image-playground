import sys
import os
from PIL import Image

loading_folder = sys.argv[1]
loading_folder = loading_folder[:-1]
saving_folder = sys.argv[2]
saving_folder = saving_folder[:-1]

# print(loading_folder, saving_folder)
# print(os.path.basename(file_name).split("."))

if not os.path.exists(saving_folder):
    os.makedirs(saving_folder)

for filename in os.listdir(loading_folder):
    full_filename = os.path.basename(filename)
    first_part_filename = os.path.basename(filename).split(".")[0]
    img = Image.open(f"./{loading_folder}/{full_filename}")
    img.save(f"./{saving_folder}/{first_part_filename}.png", "png")
