from PIL import Image
from pytesseract import image_to_string
image = Image.open("mafaheem.png")
custom_oem_psm_config = r'--tessdata-dir "C:\Program Files Ce\Tesseract-OCR\tessdata_best"'
text = image_to_string(image, lang="ara", config=custom_oem_psm_config)

import io
with io.open('mafaheem_extracted.txt','w',encoding='utf8') as f:
    f.write(str(text))