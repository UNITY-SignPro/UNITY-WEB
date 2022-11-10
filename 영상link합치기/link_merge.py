import csv
import webbrowser
import time

data = list()
f=open('human.csv','r')
rea=csv.reader(f)
for row in rea:
    data.append(row)
f.close

new_list =[]


def link(word) :
    for x,y in data :
        if word in x :
            new_list.append(y)

link('ㄱ')
link('가나')

for i in range(len(new_list)):
    url = new_list[i]
    time.sleep(5)
    webbrowser.open(url)
    
    





