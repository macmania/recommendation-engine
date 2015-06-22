import json
import csv
import pprint 
with open("math/100_math.json") as file:
    data = json.load(file)

with open("data.csv", "w") as file:
    csv_file = csv.writer(file)
    for results in data["results"]:
    	for e in results: 
    		print e

   

        #csv_file.writerow(item['title'] + [item['description'], item['subjects'][0]])