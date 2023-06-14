from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import os

# create list to hold article names
articles = []

# add all article file names to list

for article in os.listdir('Part2_Articles'):
    articles.append(("Part2_Articles/" + article))
    #print(article)

#print(len(articles))

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

CNN_TOTAL_POLARITY = 0.0
CNN_TOTAL_SUBJECTIVITY = 0.0
FOX_TOTAL_POLARITY = 0.0
FOX_TOTAL_SUBJECTIVITY = 0.0
MSNBC_TOTAL_POLARITY = 0.0
MSNBC_TOTAL_SUBJECTIVITY = 0.0
NYP_TOTAL_POLARITY = 0.0
NYP_TOTAL_SUBJECTIVITY = 0.0

for article in articles:
    polar, subject = assess_article_polarity_subjectivity(article)
    if "CNN" in article:
        CNN_TOTAL_POLARITY += polar
        CNN_TOTAL_SUBJECTIVITY += subject
    elif "FOX" in article:
        FOX_TOTAL_POLARITY += polar
        FOX_TOTAL_SUBJECTIVITY += subject
    elif "NBC" in article:
        MSNBC_TOTAL_POLARITY += polar
        MSNBC_TOTAL_SUBJECTIVITY += subject
    else:
        NYP_TOTAL_POLARITY += polar
        NYP_TOTAL_SUBJECTIVITY += subject


CNN_AVERAGE_POLARITY = CNN_TOTAL_POLARITY / 100
CNN_AVERAGE_SUBJECTIVITY = CNN_TOTAL_SUBJECTIVITY / 100
FOX_AVERAGE_POLARITY = FOX_TOTAL_POLARITY / 100
FOX_AVERAGE_SUBJECTIVITY = FOX_TOTAL_SUBJECTIVITY / 100
MSNBC_AVERAGE_POLARITY = MSNBC_TOTAL_POLARITY / 100
MSNBC_AVERAGE_SUBJECTIVITY = MSNBC_TOTAL_SUBJECTIVITY / 100
NYP_AVERAGE_POLARITY = NYP_TOTAL_POLARITY / 100
NYP_AVERAGE_SUBJECTIVITY = NYP_TOTAL_SUBJECTIVITY / 100

print("")
print("Sentiment analysis for 100 CNN, 100 Fox, 100 MSNBC, and 100 New York Post articles")
print("Article polarity score is a float within the range [-1.0, 1.0] and "
    + "reflects negative to positive perceived word choice.")
print("Article subjectivity score as a float within the range [0.0, 1.0] where "
    + "0.0 is very objective and 1.0 is very subjective.")
print("CNN average article polarity: ", CNN_AVERAGE_POLARITY)
print("CNN average article subjectivity: ", CNN_AVERAGE_SUBJECTIVITY)
print("")
print("Fox average article polarity: ", FOX_AVERAGE_POLARITY)
print("Fox average article subjectivity: ", FOX_AVERAGE_SUBJECTIVITY)
print("")
print("MSNBC average article polarity: ", MSNBC_AVERAGE_POLARITY)
print("MSNBC average article subjectivity: ", MSNBC_AVERAGE_SUBJECTIVITY)
print("")
print("New York Post average article polarity: ", NYP_AVERAGE_POLARITY)
print("New York Post average article subjectivity: ", NYP_AVERAGE_SUBJECTIVITY)
print("")


# split articles into test and train sets

TEST_ARTICLES = []
for article in os.listdir('Part2_Test_Articles'):
    TEST_ARTICLES.append("Part2_Test_Articles/" + article)

TRAINING_ARTICLES =[]
for article in os.listdir('Part2_Training_Articles'):
    TRAINING_ARTICLES.append("Part2_Training_Articles/" + article)


train = []
for article in TRAINING_ARTICLES:
    if 'CNN' in article:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'CNN'))
    elif 'FOX' in article:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'FOX'))
    elif 'NBC' in article:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'NBC'))
    else:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'NYP'))

test = []
for article in TEST_ARTICLES:
    if 'CNN' in article:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'CNN'))
    elif 'FOX' in article:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'FOX'))
    elif 'NBC' in article:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'NBC'))
    else:
        text = open(article, encoding='UTF-8')
        text = text.read()
        train.append((text, 'NYP'))

cl = NaiveBayesClassifier(train)

# Compute accuracy
print("The accuracy of our classifier is:",cl.accuracy(test))
print("\n")

cl.show_informative_features(25)
