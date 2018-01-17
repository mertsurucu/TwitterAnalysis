# -*- coding: utf-8 -*-
import json
import string
import inspect,os

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
f=open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) +'/tweet_data.json', 'r')
w=open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/term frequencies.txt','w+')
punctuation = list(string.punctuation)
stop = punctuation+['a','an','the','rt','via','to','of','for','and','or','i','in','at','on','out','with','by','de',' ','is','am','are','my','your','our','us','me','you','it','','the','no','have','has','we','her','his','them','when','who','where','which','how','that','not','this','&amp;','from','new','la','but']
cleardic={}
xaxis=[]
yaxis=[]
def p1(dic):
    for line in f:#reads every line in order
        tweet = json.loads(line) # load it as Python dict
        created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
        str=tweet['text']#tweet
        str=str.lower()
        L=str.split(" ");
        date=tweet["created_at"];#date-time in ISO format
        dt=datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y") #reading date in ISO format
        print tweet['text'].encode('utf-8')
        print L;
        print('\n')
        for i in L:
            if i not in stop:
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1
p1(cleardic)
val=cleardic.values()
val.sort(reverse=True)
for i in val[:20]:
    a=0
    for j in cleardic.keys():
        if a==0:
            if cleardic[j]==i:
                num=("%s"%(i))
                w.write("('%s',%s)\n"%(j,num))
                xaxis.append(j)
                yaxis.append(i)
                a+=1
w.close()
f.close()

#grafik cizimi
fig=plt.figure()
plt.title('histogram plot')
labels = xaxis[:20]
fig.autofmt_xdate(bottom=0.2, rotation=60, ha='right')
y=val[:20]
plt.xticks(range(20),labels, rotation='vertical')
plt.bar(range(20),y)
plt.xlim([-0.2,20])
plt.savefig('term co-occurrences.png')
plt.show()

top10=xaxis[:10]
w1=open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/term frequencies overtime.txt','w+')
w2=open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/term cooccurrences.txt','w+')
timelist1=[]
timelist2=[]
timelist3=[]
timelist4=[]
timelist5=[]
time=[]
writecount=[1,1,1,1,1,1,1,1,1,1]
b=0
print(writecount)
def p2andp3(terms):
    f1=open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) +'/tweet_data.json', 'r')
    firstmin=46
    sub=0
    top10=xaxis[:10]
    for line in f1:#reads every line in order
        tweet = json.loads(line) # load it as Python dict
        created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
        str=tweet['text']#tweet
        str=str.lower()
        L=str.split(" ");
        if terms in L:
            if terms in xaxis[:5]:
                sub=L.count(terms)+sub
            for k in range(10):
                if top10[k] in L:
                    count[k]+=1
        date=tweet["created_at"];#date-time in ISO format
        dt=datetime.strptime(date, "%a %b %d %H:%M:%S +0000 %Y") #reading date in ISO format
        datewrite=("%s" %(dt))
        if terms in xaxis[:5]:
            if firstmin!=dt.minute and dt.second==00:
                w1.write("%s %s %d \n"%(terms,datewrite,sub))
                if terms==xaxis[0]:
                    timelist1.append(sub)
                if terms==xaxis[1]:
                    timelist2.append(sub)
                if terms==xaxis[2]:
                    timelist3.append(sub)
                if terms==xaxis[3]:
                    timelist4.append(sub)
                if terms==xaxis[4]:
                    timelist5.append(sub)
                time=("%s" %(dt.time()))
                time=time[:5]
                sub=0
            firstmin=dt.minute
    print(count)
    a=0
    for j in top10:
        w2.write("%s-%s %d\n"%(terms,j,count[a]))
        a+=1

    print(writecount)
for i in xaxis[:10]:
    count=[0,0,0,0,0,0,0,0,0,0]
    print(i)
    p2andp3(i)
    writecount[b]=count
    b+=1

#grafik p2
plt.title('term frequencies a period of time')
timelist=[[timelist1],[timelist2],[timelist3],[timelist4],[timelist5]]
xstick=[]
for i in time:
    if i[-1]!="0" and i[-1]!="5":
        xstick.append(" ")
    else:
        xstick.append(i)
plt.xticks(range(23),xstick)
for j in range(5):
        plt.plot(range(23),timelist[j][0],'.-',label=xaxis[j])
plt.legend(xaxis[:5])
plt.savefig('term frequency overtime.png')
plt.show()

#grafik p3
matrix = np.matrix(writecount)
print(matrix)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal')
plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.ocean)
plt.colorbar()
plt.savefig(' term co-occurrences.png')
plt.show()





