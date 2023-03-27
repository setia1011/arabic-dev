from farasa.segmenter import FarasaSegmenter
segmenter = FarasaSegmenter()
f = open('mafaheem_extracted.txt', encoding='utf-8')
segmented = segmenter.segment(f.read())

import io
with io.open('mafaheem_segmented.txt','w',encoding='utf8') as f:
   f.write(str(segmented))