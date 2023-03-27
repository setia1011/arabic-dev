from farasa.diacratizer import FarasaDiacritizer

f = open('mafaheem_extracted.txt', encoding='utf-8')
diacritizer = FarasaDiacritizer()
diacritized = diacritizer.diacritize(f.read())

import io
with io.open('mafaheem_tashkeel_best.txt','w',encoding='utf8') as f:
   f.write(str(diacritized))