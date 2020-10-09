import pyocr
from PIL import Image
import pathlib
from natsort import natsorted

img_files = list(pathlib.Path('cutted_image').glob('*.jpeg'))
txt_dir = pathlib.Path('output_txt')
# pyocrへ利用するOCRエンジンをTesseractに指定する。
tools = pyocr.get_available_tools()
tool = tools[0]

# OCR対象の画像ファイルを読み込む
img = ''
index = '01'

for img_file in natsorted(img_files, key=lambda x: x.name):
    img = Image.open(img_file)
    # 画像から文字を読み込む
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img, lang="jpn+eng", builder=builder)

    #path_w = str(txt_dir) + '/sample02-' + index + '.php'
    path_w = txt_dir/pathlib.Path(index+'.php')
    with open(path_w, mode='w') as f:
        f.write(text)
    index = int(index) + 1
    index = "{:02d}".format(index)
