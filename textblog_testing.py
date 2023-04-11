# textblob_testing.py
#requirements:
# pip3 install textblob
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import PositiveNaiveBayesClassifier

# reference: https://youtu.be/RkbCxVwTC6s
# reference: https://stevenloria.com/simple-text-classification/
# reference: https://textblob.readthedocs.io/en/dev/index.html

text = "Today is a beautiful day"
blob = TextBlob(text)

print(blob.tags)
# [('Today', 'NN'), ('is', 'VBZ'), ('a', 'DT'), ('beautiful', 'JJ'), ('day', 'NN')]
print("\n")

print(blob.words)
# ['Today', 'is', 'a', 'beautiful', 'day']
print("\n")

print(blob.noun_phrases)
# ['beautiful day']
print("\n")

print(blob.polarity)
# 0.85
print("\n")

print(blob.subjectivity)
# 1.0
print("\n")

print(blob.sentiment)
# Sentiment(polarity=0.85, subjectivity=1.0)
# Polarity: Return the polarity score as a float within the range [-1.0, 1.0]
# Subjectivity: Return the subjectivity score as a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
print("\n")

print(blob.sentiment_assessments)
# Sentiment(polarity=0.85, subjectivity=1.0, assessments=[(['beautiful'], 0.85, 1.0, None)])
# Return a tuple of form (polarity, subjectivity, assessments ) where polarity is a float within the range [-1.0, 1.0], subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective, and assessments is a list of polarity and subjectivity scores for the assessed tokens.
print("\n")

print(blob.word_counts)
# defaultdict(<class 'int'>, {'today': 1, 'is': 1, 'a': 1, 'beautiful': 1, 'day': 1})
print("\n")

text = """Today is a beautiful day.
Tomorrow will be even better."""
blob = TextBlob(text)
print(blob.sentences)
# [Sentence("Today is a beautiful day."), Sentence("Tomorrow will be even better.")]
print("\n")

print(blob.sentences[1])
# Tomorrow will be even better.
print("\n")

# Spelling correction
text = "Today is a beutiful day"
blob = TextBlob(text)
print(blob.correct())
# Today is a beautiful day
print("\n")

# Classifier
train = [
    ("I love this sandwich.", "pos"),
    ("this is an amazing place!", "pos"),
    ("I feel very good about these beers.", "pos"),
    ("this is my best work.", "pos"),
    ("what an awesome view", "pos"),
    ("I do not like this restaurant", "neg"),
    ("I am tired of this stuff.", "neg"),
    ("I can't deal with this", "neg"),
    ("he is my sworn enemy!", "neg"),
    ("my boss is horrible.", "neg"),
]

test = [
    ('The beer was good.', 'pos'),
    ("I do not enjoy my job", "neg"),
    ("I ain't feeling dandy today.", "neg"),
    ('I feel amazing!', 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", "neg")
]

from textblob.classifiers import NaiveBayesClassifier

cl = NaiveBayesClassifier(train)

# Classify a TextBlob
blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)
print(blob.classify())

for s in blob.sentences:
    print(s, s.classify())
print("\n")

# Compute accuracy
print(cl.accuracy(test))
# 0.8333333333333334
print("\n")

# Show 5 most informative features
cl.show_informative_features(5)
# Most Informative Features
#            contains(my) = True              neg : pos    =      1.7 : 1.0
#            contains(an) = False             neg : pos    =      1.6 : 1.0
#             contains(I) = False             pos : neg    =      1.4 : 1.0
#             contains(I) = True              neg : pos    =      1.4 : 1.0
#            contains(my) = False             pos : neg    =      1.3 : 1.0
print("\n")

#b = TextBlob("I once traveled a long and bonjour road to North Hampton, Ellensburg, and Versaille.")
#b = TextBlob("bonjour")
#b.detect_language() # requires internet connection to Google API

print(blob.title())
# The Beer Is Good. But The Hangover Is Horrible.
print("\n")


# Positive Naive Bayes Classifier
sports_sentences = ['The team dominated the game',
                   'They lost the ball',
                   'The game was intense',
                   'The goalkeeper catched the ball',
                   'The other team controlled the ball']
various_sentences = ['The President did not comment',
                        'I lost the keys',
                        'The team won the game',
                        'Sara has two kids',
                        'The ball went off the court',
                        'They had the ball for the whole game',
                        'The show is over']
classifier = PositiveNaiveBayesClassifier(positive_set=sports_sentences,
                                           unlabeled_set=various_sentences)
print(classifier.classify("My team lost the game"))
# True
print("\n")
print(classifier.classify("And now for something completely different."))
# False
print("\n")

