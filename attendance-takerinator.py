import csv

with open('people.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
with open('replacements.csv', newline='') as f:
    reader = csv.reader(f)
    replacements = list(reader)

lines = []
with open ("put_the_chat_here.txt", "r") as myfile:
    lines=myfile.readlines()
text = '\n'.join(lines)

from collections import defaultdict
mappings=defaultdict(lambda: "he/she is not there in the list")
for i in data:
    mappings[i[0]]=i[1]
for i in replacements:
    del mappings[i[0]]
    mappings[i[1]]=i[2]
f = open("absentess_list.txt", "w")
f.write("------------These are the people who are absent in this meeting:--------------------\n")
present=defaultdict(lambda: False)
for i in mappings.keys():
    if text.find(i)==-1:
        f.write(i+"--"+mappings[i]+"\n")
f.close()