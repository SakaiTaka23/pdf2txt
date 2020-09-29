from PIL import Image
import sys

import pyocr
import pyocr.builders
import re

# ツールがあるか確認
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print('No OCR tool found')
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

# 出力
txt = tool.image_to_string(
    Image.open('out_img/test1page-1.png'),
    lang='jpn',
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

# 各行ごとに区切る
lines = txt.splitlines()
pages = []  # １ページずつ配列に入れる
page = ''  # データ保存用
count = 0

for line in lines:
    count += 1
    if not 'sample' in line:
        line = re.sub('^\d{1,2}', '', line)
        page += line
        if count == len(lines):
            pages.append(page)
            page = ''
    else:
        pages.append(page)
        page = ''
pages.pop(0)

# テキストデータとして出力
lecture = '01'
page_num = '01'

output_path = 'out_hw/sample'
output_path += lecture
output_path += '-'
output_path += page_num
output_path += '.php'

for page in pages:

    with open(output_path, mode='w') as w:
        w.write(page)

