__author__ = 'jojofabe'

import nltk
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
                topics_table[topic] = [{"title":data_point['title'],
                                       "publisher":data_point['publisher'],
                                       "summary":data_point['description'],
                                        }]
            else:
                 topics_table[topic].append({'title':data_point['title'],
                                       'publisher':data_point['publisher'],
                                       'summary':data_point["description"],
                                        })

for i in topics_table:
    print i








