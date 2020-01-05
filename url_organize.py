#いわゆる文字列処理，改行コードは\n．

import os

f = open('poti.sh')
txt = f.read()
f.close
text = txt.replace("\n", ".png\n")
print(text)