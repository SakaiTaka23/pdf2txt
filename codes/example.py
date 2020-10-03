from PIL import Image
import sys

import pathlib
import pdf2image

import os
import shutil

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


# pdfをページごとに画像に変換
pdf_files = pathlib.Path('in_pdf').glob('*.pdf')
img_dir = pathlib.Path('out_img')

for pdf_file in pdf_files:
    base = pdf_file.stem
    images = pdf2image.convert_from_path(pdf_file, grayscale=True)
    for index, image in enumerate(images):
        image.save(img_dir/pathlib.Path(base +
                                        '-{}.png'.format(index + 1)), 'png', resolution=200)


# 出力
png_files = pathlib.Path('out_img').glob('*.png')
txt = ''

for png_file in png_files:
    txt += tool.image_to_string(
        Image.open(png_file),
        lang='jpn',
        builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    )

# 画像ファイルを削除、作成
shutil.rmtree('out_img')
os.mkdir('out_img')


# 各行ごとに区切る


def make_output_path(lecture, page_num):
    print('out_hw/sample'+lecture+'-'+page_num+'.php')
    return 'out_hw/sample'+lecture+'-'+page_num+'.php'


def save_file(content, output_path):
    print('saving')
    with open(output_path, mode='w') as w:
        w.write(content)
    return 'ok'


lines = txt.splitlines(True)

pages = []  # １ページずつ配列に入れる
page = ''  # データ保存用
array_judge = 0

lecture = '01'  # ユーザーから受け取る
page_num = '00'  # ページ番号

for line in lines:
    array_judge += 1
    if not 'sample' in line:
        line = re.sub('^\d{1,2}', '', line)
        page += line
        if array_judge == len(lines):
            print(page_num)
            output_path = make_output_path(lecture, page_num)
            save_file(page, output_path)
            page = ''
            page_num = int(page_num)
            page_num += 1
            page_num = "{:02d}".format(page_num)
    else:
        if page_num == '00':
            page_num = int(page_num)
            page_num += 1
            page_num = "{:02d}".format(page_num)
            print(page_num)
            continue
        output_path = make_output_path(lecture, page_num)
        save_file(page, output_path)
        page = ''
        page_num = int(page_num)
        page_num += 1
        page_num = "{:02d}".format(page_num)
