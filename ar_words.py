from farasa.pos import FarasaPOSTagger
import json
import re

pos_tagger = FarasaPOSTagger()
f = open('mafaheem_extracted.txt', encoding='utf-8')
tags = pos_tagger.tag_segments(f.read())
words = []
for i in tags:
   s = json.dumps(i.__dict__, ensure_ascii=False).encode("utf-8")
   c = json.loads(s)['tokens'][0].replace("+","")
   words.append(c)

import io
with io.open('mafaheem_words.txt','w',encoding='utf8') as f:
   for o in words:
      arabic = re.findall(r'[\u0600-\u06FF]+',o)
      if len(arabic) > 0:
         if arabic[0].isalnum():
            if len(arabic[0]) > 1:
               f.write(str(arabic[0])+ '\n')
