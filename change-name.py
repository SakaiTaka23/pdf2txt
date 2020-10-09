import pathlib
from natsort import natsorted
import os

all_path = 'all_name.txt'
unchanged_files = list(pathlib.Path('input_change_name').glob('*.php'))

name = ''
with open(all_path) as f:
    name = [s.strip() for s in f.readlines()]

index = 0
for file in natsorted(unchanged_files, key=lambda x: x.name):
    os.rename(file, 'output_change_name/'+name[index])
    index += 1
