from langdetect import detect
""" https://pypi.org/project/langdetect/ """

import nltk
""" https://www.nltk.org/howto.html """

import os

af = 0  #Afrikaans
ar = 0  #Arabic
ca = 0  #Catalan
cy = 0  #Welsh
da = 0  #Danish
de = 0  #German
en = 0  #English
es = 0  #Spanish, Castilian
et = 0  #Estonian
fi = 0  #Finnish
fr = 0  #French
hr = 0  #Croatian
id = 0  #Indonesian
it = 0  #Italian
lv = 0  #Latvian
nl = 0  #Dutch, Flemish
no = 0  #Norwegian
pl = 0  #Polish
pt = 0  #Portuguese
ro = 0  #Romanian, Moldavian, Moldovan
sk = 0  #Slovak
sl = 0  #Slovenian
so = 0  #Somali
sq = 0  #Albanian
sv = 0  #Swedish
sw = 0  #Swahili
tl = 0  #Tagalog
tr = 0  #Turkish
yi = 0  #Yiddish
cs = 0  #Czech
hu = 0  #Hungarian
lt = 0  #Lithuanian
vi = 0  #Vietnamese

language = 'none'

LANGS = [af, ar, ca, cy, da, de, en, es, et, fi, fr, hr, id, it, lv, 
         nl, no, pl, pt, ro, sk, sl, so, sq, sv, sw, tl, tr, yi, cs, hu, lt, vi]

FULL_NAMES = ["Afrikaans", "Arabic", "Catalan", "Welsh", "Danish", "German", "English", "Spanish",
              "Castilian", "Estonian", "Finnish", "French", "Croatian", "Indonesian", "Italian",
              "Latvian", "Dutch, Flemish", "Norwegian", "Polish",  "Portuguese", 
              "Romanian, Moldavian, Moldovan", "Slovak", "Slovenian", "Somali",  "Albanian", "Swedish",
              "Swahili", "Tagalog", "Turkish", "Yiddish", 'Czech', 'Hungarian', 'Lithuanian', 'Vietnamese']

def reset_langs(langs):
    for item in langs:
        item = 0
"""
reset_langs(LANGS)

CNN_LANGS = []

for article in os.listdir('CNN_Articles'):
    article = 'CNN_Articles/' + article
    text = open(article, encoding='UTF-8')
    for line in text:
        if line != "\n":
            words = line.split()
            for word in words:
                try:
                    lang = str(detect(word))
                    CNN_LANGS.append(lang)
                except:
                    language = "error"
                    # Occasionally, there is an error from either a non-word
                        # getting passed or it just can't detect the language
                    #print()

#print(langs)
for lang in CNN_LANGS:
    if lang == 'af':
        LANGS[0] += 1
    elif lang == 'ar':
        LANGS[1] += 1
    elif lang == 'ca':
        LANGS[2] += 1
    elif lang == 'cy':
        LANGS[3] += 1
    elif lang == 'da':
        LANGS[4] += 1
    elif lang == 'de':
        LANGS[5] += 1
    elif lang == 'en':
        LANGS[6] += 1
    elif lang == 'es':
        LANGS[7] += 1
    elif lang == 'et':
        LANGS[8] += 1
    elif lang == 'fi':
        LANGS[9] += 1
    elif lang == 'fr':
        LANGS[10] += 1
    elif lang == 'hr':
        LANGS[11] += 1
    elif lang == 'id':
        LANGS[12] += 1
    elif lang == 'it':
        LANGS[13] += 1
    elif lang == 'lv':
        LANGS[14] += 1
    elif lang == 'nl':
        LANGS[15] += 1
    elif lang == 'no':
        LANGS[16] += 1
    elif lang == 'pl':
        LANGS[17] += 1
    elif lang == 'pt':
        LANGS[18] += 1
    elif lang == 'ro':
        LANGS[19] += 1
    elif lang == 'sk':
        LANGS[20] += 1
    elif lang == 'sl':
        LANGS[21] += 1
    elif lang == 'so':
        LANGS[22] += 1
    elif lang == 'sq':
        LANGS[23] += 1
    elif lang == 'sv':
        LANGS[24] += 1
    elif lang == 'sw':
        LANGS[25] += 1
    elif lang == 'tl':
        LANGS[26] += 1
    elif lang == 'tr':
        LANGS[27] += 1
    elif lang == 'yi':
        LANGS[28] += 1
    elif lang == "cs":
        LANGS[29] += 1
    elif lang == 'hu':
        LANGS[30] += 1
    elif lang == 'lt':
        LANGS[31] += 1
    elif lang == 'vi':
        LANGS[32] += 1
    else:
        print(lang)

print("CNN Processed Language Results:")
for i, j in zip(FULL_NAMES, LANGS):
    print(i,": ", j)

# New Section for Fox News Articles

reset_langs(LANGS)

FOX_LANGS = []

for article in os.listdir('Fox_Articles'):
    article = 'Fox_Articles/' + article
    text = open(article, encoding='UTF-8')
    for line in text:
        if line != "\n":
            words = line.split()
            for word in words:
                try:
                    lang = str(detect(word))
                    FOX_LANGS.append(lang)
                except:
                    language = "error"
                    # Occasionally, there is an error from either a non-word
                        # getting passed or it just can't detect the language

for lang in FOX_LANGS:
    if lang == 'af':
        LANGS[0] += 1
    elif lang == 'ar':
        LANGS[1] += 1
    elif lang == 'ca':
        LANGS[2] += 1
    elif lang == 'cy':
        LANGS[3] += 1
    elif lang == 'da':
        LANGS[4] += 1
    elif lang == 'de':
        LANGS[5] += 1
    elif lang == 'en':
        LANGS[6] += 1
    elif lang == 'es':
        LANGS[7] += 1
    elif lang == 'et':
        LANGS[8] += 1
    elif lang == 'fi':
        LANGS[9] += 1
    elif lang == 'fr':
        LANGS[10] += 1
    elif lang == 'hr':
        LANGS[11] += 1
    elif lang == 'id':
        LANGS[12] += 1
    elif lang == 'it':
        LANGS[13] += 1
    elif lang == 'lv':
        LANGS[14] += 1
    elif lang == 'nl':
        LANGS[15] += 1
    elif lang == 'no':
        LANGS[16] += 1
    elif lang == 'pl':
        LANGS[17] += 1
    elif lang == 'pt':
        LANGS[18] += 1
    elif lang == 'ro':
        LANGS[19] += 1
    elif lang == 'sk':
        LANGS[20] += 1
    elif lang == 'sl':
        LANGS[21] += 1
    elif lang == 'so':
        LANGS[22] += 1
    elif lang == 'sq':
        LANGS[23] += 1
    elif lang == 'sv':
        LANGS[24] += 1
    elif lang == 'sw':
        LANGS[25] += 1
    elif lang == 'tl':
        LANGS[26] += 1
    elif lang == 'tr':
        LANGS[27] += 1
    elif lang == 'yi':
        LANGS[28] += 1
    elif lang == "cs":
        LANGS[29] += 1
    elif lang == 'hu':
        LANGS[30] += 1
    elif lang == 'lt':
        LANGS[31] += 1
    elif lang == 'vi':
        LANGS[32] += 1
    else:
        print(lang)

print("Fox Processed Language Results:")
for i, j in zip(FULL_NAMES, LANGS):
    print(i,": ", j)

# New section for MSNBC news articles

reset_langs(LANGS)

MSNBC_LANGS = []

for article in os.listdir('MSNBC_Articles'):
    article = 'MSNBC_Articles/' + article
    text = open(article, encoding='UTF-8')
    for line in text:
        if line != "\n":
            words = line.split()
            for word in words:
                try:
                    lang = str(detect(word))
                    MSNBC_LANGS.append(lang)
                except:
                    language = "error"
                    # Occasionally, there is an error from either a non-word
                        # getting passed or it just can't detect the language

for lang in MSNBC_LANGS:
    if lang == 'af':
        LANGS[0] += 1
    elif lang == 'ar':
        LANGS[1] += 1
    elif lang == 'ca':
        LANGS[2] += 1
    elif lang == 'cy':
        LANGS[3] += 1
    elif lang == 'da':
        LANGS[4] += 1
    elif lang == 'de':
        LANGS[5] += 1
    elif lang == 'en':
        LANGS[6] += 1
    elif lang == 'es':
        LANGS[7] += 1
    elif lang == 'et':
        LANGS[8] += 1
    elif lang == 'fi':
        LANGS[9] += 1
    elif lang == 'fr':
        LANGS[10] += 1
    elif lang == 'hr':
        LANGS[11] += 1
    elif lang == 'id':
        LANGS[12] += 1
    elif lang == 'it':
        LANGS[13] += 1
    elif lang == 'lv':
        LANGS[14] += 1
    elif lang == 'nl':
        LANGS[15] += 1
    elif lang == 'no':
        LANGS[16] += 1
    elif lang == 'pl':
        LANGS[17] += 1
    elif lang == 'pt':
        LANGS[18] += 1
    elif lang == 'ro':
        LANGS[19] += 1
    elif lang == 'sk':
        LANGS[20] += 1
    elif lang == 'sl':
        LANGS[21] += 1
    elif lang == 'so':
        LANGS[22] += 1
    elif lang == 'sq':
        LANGS[23] += 1
    elif lang == 'sv':
        LANGS[24] += 1
    elif lang == 'sw':
        LANGS[25] += 1
    elif lang == 'tl':
        LANGS[26] += 1
    elif lang == 'tr':
        LANGS[27] += 1
    elif lang == 'yi':
        LANGS[28] += 1
    elif lang == "cs":
        LANGS[29] += 1
    elif lang == 'hu':
        LANGS[30] += 1
    elif lang == 'lt':
        LANGS[31] += 1
    elif lang == 'vi':
        LANGS[32] += 1
    else:
        print(lang)

print("MSNBC Processed Language Results:")
for i, j in zip(FULL_NAMES, LANGS):
    print(i,": ", j)
"""
# New section for New York Post news articles

reset_langs(LANGS)

NYP_LANGS = []

for article in os.listdir('NYP_Articles'):
    article = 'NYP_Articles/' + article
    text = open(article, encoding='UTF-8')
    for line in text:
        if line != "\n":
            words = line.split()
            for word in words:
                try:
                    lang = str(detect(word))
                    NYP_LANGS.append(lang)
                except:
                    language = "error"
                    # Occasionally, there is an error from either a non-word
                        # getting passed or it just can't detect the language

for lang in NYP_LANGS:
    if lang == 'af':
        LANGS[0] += 1
    elif lang == 'ar':
        LANGS[1] += 1
    elif lang == 'ca':
        LANGS[2] += 1
    elif lang == 'cy':
        LANGS[3] += 1
    elif lang == 'da':
        LANGS[4] += 1
    elif lang == 'de':
        LANGS[5] += 1
    elif lang == 'en':
        LANGS[6] += 1
    elif lang == 'es':
        LANGS[7] += 1
    elif lang == 'et':
        LANGS[8] += 1
    elif lang == 'fi':
        LANGS[9] += 1
    elif lang == 'fr':
        LANGS[10] += 1
    elif lang == 'hr':
        LANGS[11] += 1
    elif lang == 'id':
        LANGS[12] += 1
    elif lang == 'it':
        LANGS[13] += 1
    elif lang == 'lv':
        LANGS[14] += 1
    elif lang == 'nl':
        LANGS[15] += 1
    elif lang == 'no':
        LANGS[16] += 1
    elif lang == 'pl':
        LANGS[17] += 1
    elif lang == 'pt':
        LANGS[18] += 1
    elif lang == 'ro':
        LANGS[19] += 1
    elif lang == 'sk':
        LANGS[20] += 1
    elif lang == 'sl':
        LANGS[21] += 1
    elif lang == 'so':
        LANGS[22] += 1
    elif lang == 'sq':
        LANGS[23] += 1
    elif lang == 'sv':
        LANGS[24] += 1
    elif lang == 'sw':
        LANGS[25] += 1
    elif lang == 'tl':
        LANGS[26] += 1
    elif lang == 'tr':
        LANGS[27] += 1
    elif lang == 'yi':
        LANGS[28] += 1
    elif lang == "cs":
        LANGS[29] += 1
    elif lang == 'hu':
        LANGS[30] += 1
    elif lang == 'lt':
        LANGS[31] += 1
    elif lang == 'vi':
        LANGS[32] += 1
    else:
        print(lang)

print("New York Post Processed Language Results:")
for i, j in zip(FULL_NAMES, LANGS):
    print(i,": ", j)
