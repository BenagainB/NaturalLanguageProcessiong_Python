# part1_articles_sentiment.py

from textblob import TextBlob
import csv

# key_data = csv.reader(open('Part1_Articles/Part1Key.txt', 'r'), delimiter = '\t')
# article_filenames = []
# for line in key_data:
#    temp = line.split(',')
#    article_filenames.append(line[0] + '.txt')

#('Part1_Articles/Part1Key.txt')
#key_data = open('Part1_Articles/Part1Key.txt')
#key_data = key_data.read()
# for line in article_filenames:
#    print(line)

articles = ['Part1_Articles/CNN001.txt', 'Part1_Articles/CNN002.txt', 'Part1_Articles/CNN003.txt',
            'Part1_Articles/CNN004.txt', 'Part1_Articles/CNN005.txt', 'Part1_Articles/CNN006.txt',
            'Part1_Articles/CNN007.txt', 'Part1_Articles/CNN008.txt', 'Part1_Articles/CNN009.txt',
            'Part1_Articles/CNN010.txt', 'Part1_Articles/FOX001.txt', 'Part1_Articles/FOX002.txt',
            'Part1_Articles/FOX003.txt', 'Part1_Articles/FOX004.txt', 'Part1_Articles/FOX005.txt',
            'Part1_Articles/FOX006.txt', 'Part1_Articles/FOX007.txt', 'Part1_Articles/FOX008.txt',
            'Part1_Articles/FOX009.txt', 'Part1_Articles/FOX010.txt']




def assess_article_polarity_subjectivity(article):
    text = open(article)
    text = text.read()
    blob = TextBlob(text)
    #print("Article polarity score as a float within the range [-1.0, 1.0]:")
    #print(blob.polarity)
    #print("\n")

    #print("Article subjectivity score as a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective:")
    #print(blob.subjectivity)
    #print("\n")
    return blob.polarity, blob.subjectivity

def assess_article_sentiment(article):
    text = open(article)
    text = text.read()
    blob = TextBlob(text)
    print("Article sentiment:")
    print(blob.sentiment)
    # Polarity: Return the polarity score as a float within the range [-1.0, 1.0]
    # Subjectivity: Return the subjectivity score as a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
    print("\n")

#assess_article_polarity_subjectivity('CNN001.txt')

fox_total_polarity = 0.0
fox_total_subjectivity = 0.0
cnn_total_polarity = 0.0
cnn_total_subjectivity = 0.0

for article in articles:
    polar, subject = assess_article_polarity_subjectivity(article)
    if "FOX" in article:
        fox_total_polarity += polar
        fox_total_subjectivity += subject
        #print("Fox polarity: ", polar)
        #print("Fox subjectivity: ", subject)
    else:
        cnn_total_polarity += polar
        cnn_total_subjectivity += subject
        #print("CNN polarity: ", polar)
        #print("CNN subjectivity: ", subject)


print("Fox total polarity: ", fox_total_polarity)
print("Fox total subjectivity: ", fox_total_subjectivity)

print("CNN total polarity: ", cnn_total_polarity)
print("CNN total subjectivity: ", cnn_total_subjectivity)
    #print(article, assess_article_sentiment(article))


#article = open(articles[0])
#text = article.read()
#blob = TextBlob(text)
