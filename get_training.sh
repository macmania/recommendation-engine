#!/bin/bash

declare -a Folder_name=("bio" "comp" "math" "philosophy" "physics");
declare -a Amount=(100 500 700 1000 1500 2000);

for f_name in Folder_name
do 
	for i in Amount
	do
		echo ${f_name};
		#curl -H "Content-Type: application/json"  "https://osf.io/api/v1/share/search/?q=subjects:"${f_name}"*ANDsize="${i} > ${f_name}/${i}_${f_name}.json
	done
done