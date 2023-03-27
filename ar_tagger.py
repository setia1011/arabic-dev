from farasa.pos import FarasaPOSTagger
from farasa.ner import FarasaNamedEntityRecognizer
from farasa.diacratizer import FarasaDiacritizer
from farasa.segmenter import FarasaSegmenter
from farasa.stemmer import FarasaStemmer
import json

pos_tagger = FarasaPOSTagger()
# "والفرق بين وصف الأفعال بالخير"
y = pos_tagger.tag_segments("والفرق بين وصف الأفعال بالخير")
l = []
for i in y:
   s=json.dumps(i.__dict__, ensure_ascii=False).encode("utf-8")
   c = json.loads(s)['tokens'][0].replace("+","")
   l.append(c)

import io
with io.open('mafaheem_baka.txt','w',encoding='utf8') as f:
   for o in l:
      f.write(str(o)+ '\n')

# f = open('mafaheem_extracted.txt', encoding='utf-8')

# pos_tagged = pos_tagger.tag_segments(f.read())

# import io
# with io.open('mafaheem_tagsss.txt','w',encoding='utf8') as f:
#    f.write(str(pos_tagged))
# import pickle
# f = open('mafaheem_tagsss.txt', encoding='utf-8')
# print(pickle.dumps(f.read()))