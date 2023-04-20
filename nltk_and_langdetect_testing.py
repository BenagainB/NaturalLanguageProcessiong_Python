# import langdetect
from langdetect import detect
""" https://pypi.org/project/langdetect/ """

import nltk
""" https://www.nltk.org/howto.html """

def clean_text(text):
    text = text.replace('\'', '')
    text = text.replace(',', '')
    text = text.replace('.', '')
    return text

sentence = "You can't always get what you want, but if you try sometimes, you just might find you get what you need."

# sentence = clean_text(sentence)

sentence_lang = detect(sentence)
print(sentence_lang)

tokens = nltk.word_tokenize(sentence, preserve_line=True)
for word in tokens:
    print(word)


tagged = nltk.pos_tag(tokens)
print(tagged)
