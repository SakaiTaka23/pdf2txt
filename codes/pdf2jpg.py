import pathlib
import pdf2image

pdf_files = pathlib.Path('in_pdf').glob('*.pdf')
img_dir = pathlib.Path('out_img')

for pdf_file in pdf_files:
    base = pdf_file.stem
    images = pdf2image.convert_from_path(pdf_file, grayscale=True)
    for index, image in enumerate(images):
        image.save(img_dir/pathlib.Path(base + '-{}.png'.format(index + 1)),'png',resolution=200)
