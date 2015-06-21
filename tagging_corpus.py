__author__ = 'jojofabe'

from nltk.corpus import stopwords
import json


'''
    setting up topics, description and title
'''
topics_table = {}

#may need to tweak this a little
with open('comp/100_comp.json') as data_file:
    data = json.load(data_file)

results = data['results']

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


'''
We want to improve data quality here by removing words that appear the most
frequent, the sole being is that we want to improve the sub-categorization of
the data point
'''


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











