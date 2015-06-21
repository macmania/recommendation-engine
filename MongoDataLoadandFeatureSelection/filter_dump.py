import pymongo
import os
from pymongo import MongoClient
import pprint
import re
import unicodedata
import string
from string import digits

def setupMongo():
    client= MongoClient()
    db = client.sharedata
    return db
def filter_features(db):
    print "testing"
    count =1
    collection= db.database
    #print collection
    fp = open('reviewsinformation_task2.csv','w')
    # get reviews who subject information size is greater than or equal to 1
    for reviews in collection.find({},{'_id':1,'title':1,'description':1,'contributors.name':1,'subjects':1}).limit(10):
    # for reviews in collection.find({'subjects': {'$not':{'$size' :0}}},{'_id':1,'title':1,'description':1,'contributors.name':1,'subjects':1}):
        contributors = reviews['contributors']
        #print reviews['_id'],'\n'
        temp = filter(lambda x: x in string.printable, reviews['description'])
        # check is string has only numbers, which is not required for this use case
        if(len(str(temp.strip(''))) == 0):
            #print "description empty
            continue;

        #print temp
        # no need to get documents without any description

        text = unicodedata.normalize('NFKD',reviews['description']).encode('ascii','ignore').replace("\r", " ").replace("\n", " ").replace("\t", '').replace("\"", "")
        temp = re.sub(r"[^a-zA-Z'  ]",' ',temp)
        #print type(temp)
        if (len(str(temp))==0):
            continue
        #print type(temp)
        #print type(text)
        text = text.lower()
        #print type(text)
        #print isinstance(text.encode("utf8"),str)
        #print "description is ",text,reviews['_id'];
        #pprint.pprint(reviews['subjects']

        count = count + 1
        print "line ",count


        contributor_list=[]
        #print count

        for contributor in contributors:
            for names in contributor.values():
                names =  unicodedata.normalize('NFKD',names).encode('ascii','ignore').replace("\r", "").replace("\n", "").replace("\t",'').replace("\"", "")
                names = re.sub(r"[^\w  ]",'',str(names).lower())
                #print names
                contributor_list.append(names)
                print "writing into file"
                fp.write(reviews['title']+',"'+text.encode('utf8')+'","'+' '.join(contributor_list)+'"\n')
    fp.close()

db=setupMongo()
filter_features(db)
