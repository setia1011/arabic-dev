import mishkal.tashkeel
vocalizer = mishkal.tashkeel.TashkeelClass()
f = open('mafaheem_extracted.txt', encoding='utf-8')
a = vocalizer.tashkeel(f.read())

import io
with io.open('mafaheem_tashkeel_alternative.txt','w',encoding='utf8') as f:
   f.write(str(a))