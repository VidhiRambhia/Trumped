import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
#import FakeNewsClassifier.
#1: unreliable
#0: reliable
'''
train=pd.read_csv('train_fake.csv')
test=pd.read_csv('test_fake.csv')
test.info()
test['label']='t'
train.info()



#data prep
test=test.fillna(' ')
train=train.fillna(' ')
test['total']=test['title']+' '+test['author']+test['text']
train['total']=train['title']+' '+train['author']+train['text']

#tfidf
#GET VECTOR COUNT
count_vectorizer = CountVectorizer(ngram_range=(1, 2))
counts = count_vectorizer.fit_transform(train['total'].values)

#SAVE WORD VECTOR
  
pickle.dump(count_vectorizer.vocabulary_, open("count_vector_fake.pkl","wb"))


#TRANSFORM WORD VECTOR TO TF IDF
transformer = TfidfTransformer(smooth_idf=False)
tfidf = transformer.fit_transform(counts)
#SAVE TF-IDF
pickle.dump(transformer, open("tfidf_fake.pkl","wb"))

targets = train['label'].values
test_counts = count_vectorizer.transform(test['total'].values)
test_tfidf = transformer.fit_transform(test_counts)

#split in samples

X_train, X_test, y_train, y_test = train_test_split(tfidf, targets, random_state=0)


logreg = LogisticRegression(C=1e5)
logreg.fit(X_train, y_train)

pickle.dump(logreg, open("logreg_fake.pkl", "wb"))


'''

category_list = ["sport", "world", "us", "business", "health", "entertainment", "sci_tech"]

text = '''House Dem Aide: We Didnâ€™t Even See Comeyâ€™s Letter Until Jason Chaffetz Tweeted It By Darrell Lucus on October 30, 2016 Subscribe Jason Chaffetz on the stump in American Fork, Utah ( image courtesy Michael Jolley, available under a Creative Commons-BY license) 
With apologies to Keith Olbermann, there is no doubt who the Worst Person in The World is this weekâ€“FBI Director James Comey. But according to a House Democratic aide, it looks like we also know who the second-worst person is as well. It turns out that when Comey sent his now-infamous letter announcing that the FBI was looking into emails that may be related to Hillary Clintonâ€™s email server, the ranking Democrats on the relevant committees didnâ€™t hear about it from Comey. They found out via a tweet from one of the Republican committee chairmen. 
As we now know, Comey notified the Republican chairmen and Democratic ranking members of the House Intelligence, Judiciary, and Oversight committees that his agency was reviewing emails it had recently discovered in order to see if they contained classified information. Not long after this letter went out, Oversight Committee Chairman Jason Chaffetz set the political world ablaze with this tweet. FBI Dir just informed me, ""The FBI has learned of the existence of emails that appear to be pertinent to the investigation."" Case reopened 
â€” Jason Chaffetz (@jasoninthehouse) October 28, 2016 
Of course, we now know that this was not the case . Comey was actually saying that it was reviewing the emails in light of â€œan unrelated caseâ€â€“which we now know to be Anthony Weinerâ€™s sexting with a teenager. But apparently such little things as facts didnâ€™t matter to Chaffetz. The Utah Republican had already vowed to initiate a raft of investigations if Hillary winsâ€“at least two yearsâ€™ worth, and possibly an entire termâ€™s worth of them. Apparently Chaffetz thought the FBI was already doing his work for himâ€“resulting in a tweet that briefly roiled the nation before cooler heads realized it was a dud. 
But according to a senior House Democratic aide, misreading that letter may have been the least of Chaffetzâ€™ sins. That aide told Shareblue that his boss and other Democrats didnâ€™t even know about Comeyâ€™s letter at the timeâ€“and only found out when they checked Twitter. â€œDemocratic Ranking Members on the relevant committees didnâ€™t receive Comeyâ€™s letter until after the Republican Chairmen. In fact, the Democratic Ranking Members didnâ€™ receive it until after the Chairman of the Oversight and Government Reform Committee, Jason Chaffetz, tweeted it out and made it public.â€ 
So letâ€™s see if weâ€™ve got this right. The FBI director tells Chaffetz and other GOP committee chairmen about a major development in a potentially politically explosive investigation, and neither Chaffetz nor his other colleagues had the courtesy to let their Democratic counterparts know about it. Instead, according to this aide, he made them find out about it on Twitter. 
There has already been talk on Daily Kos that Comey himself provided advance notice of this letter to Chaffetz and other Republicans, giving them time to turn on the spin machine. That may make for good theater, but there is nothing so far that even suggests this is the case. After all, there is nothing so far that suggests that Comey was anything other than grossly incompetent and tone-deaf. 
What it does suggest, however, is that Chaffetz is acting in a way that makes Dan Burton and Darrell Issa look like models of responsibility and bipartisanship. He didnâ€™t even have the decency to notify ranking member Elijah Cummings about something this explosive. If that doesnâ€™t trample on basic standards of fairness, I donâ€™t know what does. 
Granted, itâ€™s not likely that Chaffetz will have to answer for this. He sits in a ridiculously Republican district anchored in Provo and Orem; it has a Cook Partisan Voting Index of R+25, and gave Mitt Romney a punishing 78 percent of the vote in 2012. Moreover, the Republican House leadership has given its full support to Chaffetzâ€™ planned fishing expedition. But that doesnâ€™t mean we canâ€™t turn the hot lights on him. After all, he is a textbook example of what the House has become under Republican control. And he is also the Second Worst Person in the World. About Darrell Lucus 
Darrell is a 30-something graduate of the University of North Carolina who considers himself a journalist of the old school. An attempt to turn him into a member of the religious right in college only succeeded in turning him into the religious right's worst nightmare--a charismatic Christian who is an unapologetic liberal. His desire to stand up for those who have been scared into silence only increased when he survived an abusive three-year marriage. You may know him on Daily Kos as Christian Dem in NC . Follow him on Twitter @DarrellLucus or connect with him on Facebook . Click here to buy Darrell a Mello Yello. Connect"'''

docs_new="House Dem Aide: We Didnâ€™t Even See Comeyâ€™s Letter Until Jason Chaffetz Tweeted It"+' '+'''Darrell Lucus'''+' '+text

#docs_new = "Messi joins other football team"
docs_new = [docs_new]

#LOAD MODEL

loaded_vec = CountVectorizer(vocabulary=pickle.load(open("count_vector_fake.pkl", "rb")))
loaded_tfidf = pickle.load(open("tfidf_fake.pkl","rb"))
loaded_model = pickle.load(open("logreg_fake.pkl","rb"))

X_new_counts = loaded_vec.transform(docs_new)
X_new_tfidf = loaded_tfidf.transform(X_new_counts)
predicted = loaded_model.predict(X_new_tfidf)

print(predicted[0])