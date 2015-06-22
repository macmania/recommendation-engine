'''
Aim is to remove any unnecesary on the data set, to improve the processing speed,
we will be storing the data-sets in a folder + the individual json files for each
research paper.

Not sure if this shows any improvement in the processing speed. This could be
spear-headed by someone if anyone wants to volunteer
'''

import json

class sanitize_corpus:
    def json_to_txt(self):
        if(self.set_text_files): #sets up json to text files, this is aimed to those
                                 #that want to play around with the data
            x = ''
        elif(self.set_db): #sets up the database pymongo
            x = ''

    '''
        Remove any inconsistencies with the summary, i.e. remove any characters that
        do not yield any value with the analysis
    '''
    def remove_garbage(self):
        x = ''

    def set_env(self):
        if(self.user_input == 'text'):
            self.set_text_files = True
        else:
            self.set_db = False
