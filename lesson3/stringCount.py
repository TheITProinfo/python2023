# coding=utf-8
txtstring=""" it was the best of times it was the worst of times.
             it was the age of wisdom it was the age of foolishness."""
txtstring=txtstring.replace('.','')
txtlist=txtstring.split()
wordfrequency=[]
for w in txtlist:
    wordfrequency.append(txtlist.count(w))

mydict=dict(zip(txtlist,wordfrequency))
print(mydict)