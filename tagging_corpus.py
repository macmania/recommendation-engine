__author__ = 'jojofabe'

from nltk.corpus import stopwords
import json
import nltk
from nltk import word_tokenize,sent_tokenize

nltk.download('punkt')
'''
    setting up topics, description and title
'''
topics_table = {}

#may need to tweak this a little
with open('comp/100_comp.json') as data_file:
    data = json.load(data_file)

results = data['results']

def setUpTopicsToDictionary():
    #loading the topics into the dictionary
    for data_point in results:
        for s in data_point['subjects']:
            if '-' in s:
                subject = s
                topic = subject[subject.index('-')+2: len(subject)]
                if topic not in topics_table:
                    if data_point['publisher']["name"] != '':
                        topics_table[topic] = [{"title":data_point['title'],
                                           "publisher":data_point['publisher']["name"],
                                           "summary":data_point['description'],
                                            }]
                    else:
                        topics_table[topic] = [{"title":data_point['title'],
                                           "summary":data_point['description'],
                                            }]
                else:
                     topics_table[topic].append({'title':data_point['title'],
                                           'publisher':data_point['publisher'],
                                           'summary':data_point["description"],
                                            })



topics_table_title = {}
topics_table_description = {}

built_topic_stop_words = {}
'''
We want to improve data quality here by removing words that appear the most
frequent, the sole being is that we want to improve the sub-categorization of
the data point
'''
# essentially we are finding the most common nouns in each topic, reason being is
# to only count the ones that actually say something meaningful
# Was this effective? Setting up own stop words,
# The down-ward setbacks would be the missed words that actually are important,
# how do we find that they are important?
# How much is enough words to remove?
# Will this improve anything? Definitely questions that needs answered
def setUpOwnSubjectStopWords():

    x = {}

#figure out which is the best model
def setUpContextTitleDescriptionTable():
    x = {}

#these are better object holders for storing the topics and description, for now,
#readability wise, it's much better
def setUpStopWordsTopicDescription():
    stop_words = stopwords.words("english")
    #remove words in topics_table if they appear in stop_words
    for topic in topics_table:
        topics_table_title[topic] = []
        for element in topic:
            #[word for word in text.split() if word not in cachedStopWords]
            temp_descriptor = [word for word in element["description"].text() if word not in stop_words];
            topics_table_title[topic].append(temp_descriptor)

            temp_title = [w for w in element["title"].text() if w not in stop_words]
            topics_table_description[topic].append(temp_title)



'''
This is the second iteration of filtering through and getting the important
and relevant words

This is the experimental part in which we try to see which words would
yield the most pertinent information
'''
topics_table_nouns = {}
for topic in topics_table:
    topics_table_nouns[topic] = []
    for element in topic:
        #this extracts the noun
        topics_table_nouns[topic].append('');




'''
methods to call to set up everything
'''
setUpTopicsToDictionary()
setUpStopWordsTopicDescription()



