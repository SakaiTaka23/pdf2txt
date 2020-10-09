import re

short_path = 'short_name.txt'
all_path = 'all_name.txt'

def get_names(names):
    names = names.split('.')
    basename = names[0]
    extention = names[1]

    if '{' in basename:
        basename = re.split('[{~}]', basename)
        min = basename[1]
        max = basename[2]

        with open(all_path, mode='a') as dis:
            while int(min) <= int(max):
                dis.write(basename[0]+min+'.'+extention)
                min = str(int(min) + 1)

    else:
        with open(all_path, mode='a') as dis:
            dis.write(basename+'.'+extention)


# get_names('sample12-{15~21}.php')
# get_names('sample12-34_IE.htm')

with open(short_path) as src:
    for line in src:
        get_names(line)
