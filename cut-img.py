from PIL import Image
import pathlib
from natsort import natsorted


img_files = list(pathlib.Path('input_hw_image').glob('*.jpeg'))
img_dir = pathlib.Path('cutted_image')

index = 1

for img_file in natsorted(img_files, key=lambda x: x.name):
    im = Image.open(img_file)
    im_crop = im.crop((119, 113, 1244, 2068))
    im_crop.save(img_dir / pathlib.Path(str(index)+'.jpeg'), quality=95)
    index += 1

# cutto 1526 2070
# berore 1645*2334

# OK/sample02-1.jpeg 1	467 2212 1 2
# OK/sample02-1.jpeg 1	1 28 1399 2297
# OK/sample02-1.jpeg 1	119 113 1244 2068
