__author__ = 'jojofabe'

from nltk.corpus import stopwords
from nltk import FreqDist
import json
import nltk
import time
from nltk.tag.hunpos import HunposTagger


from nltk import word_tokenize,sent_tokenize

nltk.download('punkt')
'''
    setting up topics, description and title
'''
topics_table = {}
topics_table_zipped = {} #the summary is appended so we get table[topic] = "summary"
#may need to tweak this a little
#but for now, we want to work with a small data-set
with open('../data_dump/comp/500_comp.json') as data_file:
    data = json.load(data_file)

results = data['results']
length_results = len(results) #number of data points

#print results

#removes new lines and other inconsistencies with the data
def remove_garbage(summary):
    return summary.replace('\n\t', '')

# based on the search api that Share provides, we find that there is only
# one conjunction with the subjects - that is [* and *].
# Since we need to save the sub-categories to get more granular results
# with the classifier. Having more sub-categories will provide a better
# way in delivering more data-sets for subjects.

def has_more_subjects(topic):
    list_topics = []
    if("and" in topic): #must split the two categories
        print topic
        toks = nltk.word_tokenize(topic)
        time.sleep(1.5)
        print nltk.pos_tag(toks)

        # [(u'tissues', 'NNS'), (u'and', 'CC'), (u'organs', 'NNS')]
        # [(u'computer', 'NN'), (u'vision', 'NN'), (u'and', 'CC'), (u'pattern', 'NN'), (u'recognition', 'NN')]
        for sub in toks:
            if len(toks) > 4 and (toks[1][1] == 'CC' or toks[2][1] == 'CC'): #this means
                                                # that there is conjuction
                #try and parse this data 
                x = 0

        list_topics = topic.split("and")


def setUpTopicsToDict():
    #loading the topics into the dictionary
    for data_point in results:
        for s in data_point['subjects']:
            if "computer science" in s and '-' in s:
                subject = s
                topic = subject[subject.index('-')+2: len(subject)]
                #print topic
                #time.sleep(1.5)
                summary_sanitized = remove_garbage(data_point['description'])
                topic_sanitized = has_more_subjects(topic)

                if(topic_sanitized):
                    x = 0
                else:
                    x = 0

                if topic not in topics_table:
                    topic_sanitized = has_more_subjects(topic)
                    topics_table[topic] = [{
                                            "title":data_point['title'],
                                            "summary":summary_sanitized,
                                          }]
                else:
                    topics_table[topic].append({
                        'title' : data_point['title'],
                        'summary' : summary_sanitized
                    })

#temporary print, prints the description and title in the topics_table
setUpTopicsToDict()

for topic in topics_table:
    print topic

#print topics_table
#for e in topics_table:
    #print "here", topics_table[e]


topics_table_title = {}
topics_table_description = {}

built_topic_stop_words = {}
built_topic_context = {} #we take the most contextual nouns of each description
#and put tags on the context

topics_table_noun_only_title = {}
topics_table_noun_only_description = {}

#setting up the nouns from the corpus, we make this assumption
#good research papers are not opinionated, they are technical, use specified
#words to ensure their message and findings are published successfully. This is a
#an observation based on me <jouella>'s observation with research. As thus
#we only care about nouns.
def setUpNounsTopicTable():
    all_description = ''
    all_topics = ''
    for topic in topics_table:
        for elem in topics_table[topic]:
            #print "element:", elem
            for e in elem:
                #print e, topics_table[topic][elem]
                if(len(elem["summary"]) > 8):
                    all_description += str(elem["summary"])
                if(len(elem["title"]) > 8):
                    all_topics += str(elem["title"])

            current_description_tag = nltk.pos_tag(all_description.split())

            topics_table_noun_only_description[topic] = [noun for noun, pos in current_description_tag if pos == 'NNP']

            current_topic_tag = nltk.pos_tag(all_topics.split())
            topics_table_noun_only_title[topic] = [noun for noun, pos in current_topic_tag if pos == 'NNP']
            #print "nouns: \t",topics_table_noun_only_title[topic]
            #time.sleep(.5)
            #print topics_table_noun_only_title[topic]


    print topics_table_noun_only_description
    print topics_table_noun_only_title

    #Start print statement
    '''
    for key in topics_table_noun_only_description:
        print key, topics_table_noun_only_description[key], '\n'
    '''
    #end print statement

    # this needs more more work in setting up.

'''
We want to improve data quality here by removing words that appear the most
frequent, the sole being is that we want to improve the sub-categorization of
each point
'''
# essentially we are finding the most common nouns in each topic, reason being is
# to only count the ones that actually say something meaningful
# Was this effective? Setting up own stop words,
# The down-ward setbacks would be the missed words that actually are important,
# how do we find that they are important?
# How much is enough words to remove?
# Will this improve anything? Definitely questions that needs answered
def setUpOwnSubjectStopWords():
    for topic in topics_table_noun_only_title:
        #only limiting it to a specified length

        #might want to look into the numeric part
        all_description = [ds for ds in topics_table_noun_only_description[topic] if len(ds) > 5].join()
        all_topics = [topics for topics in topics_table_noun_only_title[topic] if len(ds) > 5].join()

        fdist_description = FreqDist(all_description)
        fidst_topics = FreqDist(all_topics)

        ten_most_common_descr = fdist_description.most_common(10)
        ten_most_common_topic = fdist_description.most_common(10)
        built_topic_stop_words[topic] = [word for word,freq in ten_most_common_descr ]
        built_topic_stop_words[topic].append([word for word, freq in ten_most_common_topic])


    print built_topic_stop_words
    print built_topic_stop_words
        #here we set up the top 5-10 words (we need to look into the data more to find
        #the hard margin of the good numerical value to stop, but for simplicity sake, we
        #pick 5 for now, let's see how our accuracy changes when change the most frequent words

'''
    for topic in built_topic_stop_words:
        print built_topic_stop_words[topic]
        print "\n"
'''

# this is a cool way to find the features of the data set and how they aggregate with one another
# might be cool to visualize, perhaps certain names appear more often - might want to look into
# data integrity of a particular data set - gives you some statistical analysis of how data is
# flawed
def setUpClusteringOnWords():
    x = {}

# set up a model in which the neighboring words are taken into consideration, this is simply
# annotating each words to come up with the best way of adding tags, might give more
# pertinent information on the relativeness of a particular data-set
def setUpContextTitleDescriptionTable():
    x = {}

#these are better object holders for storing the topics and description, for now,
#readability wise, it's much better
def setUpStopWordsTopicDescription():
    stop_words = stopwords.words("english")
    temp_descriptor = []
    #remove words in topics_table if they appear in stop_words
    for topic in topics_table:
        topics_table_title[topic] = []
        for element in topics_table[topic]:
            for w in element:
                #temp_descriptor.append(word for word in w["description"].text() if word not in stop_words)
                topics_table_title[topic].append(temp_descriptor)

            temp_title = [w for w in element["title"] if w not in stop_words]
            #description needs to be parsed and remove any inconsistencies - with the next lines

            #topics_table_description[topic].append(temp_title) #just add the title for now
    print  topics_table_description, topics_table_title
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


#setUpStopWordsTopicDescription()
#setUpNounsTopicTable()
#setUpOwnSubjectStopWords()


print topics_table_noun_only_title



#print '\n\n', topics_table_nouns
#print topics_table_noun_only_description


#setUpStopWordsTopicDescription()



