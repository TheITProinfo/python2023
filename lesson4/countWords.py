# coding=utf-8
import pprint
txtString="""it was the best of times it was the worst of times.
            it was the age of wisdom it was the age of follishness."""

txtString=txtString.replace(".","")
txtString=txtString.split()
wordfreauency=[]
for words in txtString:
    wordfreauency.append(txtString.count(words))

newdata=list(zip(txtString,wordfreauency))
newdata2=dict(zip(txtString,wordfreauency))

#print(txtString)
# print(wordfreauency)
# print(newdata)
#print(newdata2)
pprint.pprint(newdata2)
