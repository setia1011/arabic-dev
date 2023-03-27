from farasa.pos import FarasaPOSTagger
from farasa.ner import FarasaNamedEntityRecognizer
from farasa.diacratizer import FarasaDiacritizer
from farasa.segmenter import FarasaSegmenter
from farasa.stemmer import FarasaStemmer

named_entity_recognizer = FarasaNamedEntityRecognizer()
f = open('mafaheem_tashkeel_best.txt', encoding='utf-8')

named_entity_recognized = named_entity_recognizer.recognize(f.read())

import io
with io.open('mafaheem_entities.txt','w',encoding='utf8') as f:
   f.write(str(named_entity_recognized))