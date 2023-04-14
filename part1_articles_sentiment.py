# part1_articles_sentiment.py
""" initial look at articles for differences in subjectivity and polarity"""

from textblob import TextBlob

articles = ['Part1_Articles/CNN001.txt', 'Part1_Articles/CNN002.txt', 'Part1_Articles/CNN003.txt',
            'Part1_Articles/CNN004.txt', 'Part1_Articles/CNN005.txt', 'Part1_Articles/CNN006.txt',
            'Part1_Articles/CNN007.txt', 'Part1_Articles/CNN008.txt', 'Part1_Articles/CNN009.txt',
            'Part1_Articles/CNN010.txt', 'Part1_Articles/FOX001.txt', 'Part1_Articles/FOX002.txt',
            'Part1_Articles/FOX003.txt', 'Part1_Articles/FOX004.txt', 'Part1_Articles/FOX005.txt',
            'Part1_Articles/FOX006.txt', 'Part1_Articles/FOX007.txt', 'Part1_Articles/FOX008.txt',
            'Part1_Articles/FOX009.txt', 'Part1_Articles/FOX010.txt']

def assess_article_polarity_subjectivity(passage):
    """ returns 2 values: polarity and subjectivity for the passage"""
    text = open(passage, encoding='UTF-8')
    text = text.read()
    blob = TextBlob(text)
    #print("Article polarity score as a float within the range [-1.0, 1.0]:")
    #print(blob.polarity)
    #print("\n")

    #print("Article subjectivity score as a float within the range [0.0, 1.0]
        # where 0.0 is very objective and 1.0 is very subjective:")
    #print(blob.subjectivity)
    #print("\n")
    return blob.polarity, blob.subjectivity

def assess_article_sentiment(passage):
    """ returns polarity and subjectivity score for passage as a couplet """
    text = open(passage, encoding='UTF-8')
    text = text.read()
    blob = TextBlob(text)
    print("Article sentiment:")
    print(blob.sentiment)
    # Polarity: Return the polarity score as a float within the range [-1.0, 1.0]
    # Subjectivity: Return the subjectivity score as a float within the range [0.0, 1.0]
        # where 0.0 is very objective and 1.0 is very subjective.
    print("\n")

FOX_TOTAL_POLARITY = 0.0
FOX_TOTAL_SUBJECTIVITY = 0.0
CNN_TOTAL_POLARITY = 0.0
CNN_TOTAL_SUBJECTIVITY = 0.0

for article in articles:
    polar, subject = assess_article_polarity_subjectivity(article)
    if "FOX" in article:
        FOX_TOTAL_POLARITY += polar
        FOX_TOTAL_SUBJECTIVITY += subject
        #print("Fox polarity: ", polar)
        #print("Fox subjectivity: ", subject)
    else:
        CNN_TOTAL_POLARITY += polar
        CNN_TOTAL_SUBJECTIVITY += subject
        #print("CNN polarity: ", polar)
        #print("CNN subjectivity: ", subject)

FOX_AVERAGE_POLARITY = FOX_TOTAL_POLARITY / 10
FOX_AVERAGE_SUBJECTIVITY = FOX_TOTAL_SUBJECTIVITY / 10
CNN_AVERAGE_POLARITY = CNN_TOTAL_POLARITY / 10
CNN_AVERAGE_SUBJECTIVITY = CNN_TOTAL_SUBJECTIVITY / 10

print("")
print("Sentiment analysis for 10 CNN and 10 Fox articles")
print("Article polarity score is a float within the range [-1.0, 1.0] and "
    + "reflects negative to positive perceived word choice.")
print("Article subjectivity score as a float within the range [0.0, 1.0] where "
    + "0.0 is very objective and 1.0 is very subjective.")
print("Fox average article polarity: ", FOX_AVERAGE_POLARITY)
print("Fox average article subjectivity: ", FOX_AVERAGE_SUBJECTIVITY)
print("")
print("CNN average article polarity: ", CNN_AVERAGE_POLARITY)
print("CNN average article subjectivity: ", CNN_AVERAGE_SUBJECTIVITY)
print("These articles act as our training set to see if naive bayes can" +
    " differentiate CNN from Fox articles.")

# Assuming a good size for a test set is 60% the size of the training set, we need 12 more articles

PART_2_ARTICLES =['Part1_Test_Articles/CNN011.txt', 'Part1_Test_Articles/CNN012.txt',
                'Part1_Test_Articles/CNN013.txt', 'Part1_Test_Articles/CNN014.txt',
                'Part1_Test_Articles/CNN015.txt', 'Part1_Test_Articles/CNN016.txt',
                'Part1_Test_Articles/FOX011.txt', 'Part1_Test_Articles/FOX012.txt',
                'Part1_Test_Articles/FOX013.txt', 'Part1_Test_Articles/FOX014.txt',
                'Part1_Test_Articles/FOX015.txt', 'Part1_Test_Articles/FOX016.txt']

train = []
for article in articles:
    if 'FOX' in article:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'FOX'))
    else:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'CNN'))

test = []
for article in PART_2_ARTICLES:
    if 'FOX' in article:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'FOX'))
    else:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'CNN'))
