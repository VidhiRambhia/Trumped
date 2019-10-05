import pandas
import glob
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split


with open('news', 'r') as f:
    text = f.read()
    news = text.split("\n\n")
    count = {'sport': 0, 'world': 0, "us": 0, "business": 0, "health": 0, "entertainment": 0, "sci_tech": 0}
    counter=0
    for news_item in news:
        counter = counter +1
        if(counter>1433):
            break
        lines = news_item.split("\n")
        file_to_write = open('data/' + lines[6] + '/' + str(count[lines[6]]) + '.txt', 'w+')
        count[lines[6]] = count[lines[6]] + 1
        file_to_write.write(news_item)  # python will convert \n to os.linesep
        file_to_write.close()




category_list = ["sport", "world", "us", "business", "health", "entertainment", "sci_tech"]
directory_list = ["data/sport/*.txt", "data/world/*.txt","data/us/*.txt","data/business/*.txt","data/health/*.txt","data/entertainment/*.txt","data/sci_tech/*.txt",]

text_files = list(map(lambda x: glob.glob(x), directory_list))
text_files = [item for sublist in text_files for item in sublist]

training_data = []


for t in text_files:
    f = open(t, 'r')
    f = f.read()
    t = f.split('\n')
    training_data.append({'data' : t[0] + ' ' + t[1], 'flag' : category_list.index(t[6])})
    
training_data[0]

training_data = pandas.DataFrame(training_data, columns=['data', 'flag'])
training_data.to_csv("train_data_type.csv", sep=',', encoding='utf-8')
print(training_data.data.shape)




#GET VECTOR COUNT
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(training_data.data)

#SAVE WORD VECTOR
pickle.dump(count_vect.vocabulary_, open("count_vector_type.pkl","wb"))



#TRANSFORM WORD VECTOR TO TF IDF
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#SAVE TF-IDF
pickle.dump(tfidf_transformer, open("tfidf_type.pkl","wb"))

# Multinomial Naive Bayes



#clf = MultinomialNB().fit(X_train_tfidf, training_data.flag)
X_train, X_test, y_train, y_test = train_test_split(X_train_tfidf, training_data.flag, test_size=0.25, random_state=42)
clf = MultinomialNB().fit(X_train, y_train)

#SAVE MODEL
pickle.dump(clf, open("nb_model_type.pkl", "wb"))



category_list = ["sport", "world", "us", "business", "health", "entertainment", "sci_tech"]

docs_new = str(" farmer in Adairville, Ky. is expecting his profit to vanish this year, largely because of the confluence of falling crop prices and rising costs for seeds and other materials. The price of an   bag of seed corn rose to $300 from $80 in the last decade, as the companies that produced them consolidated, he said. And with the recent decline in commodity prices, Mr. Halcomb said he expects to lose $100 an acre this year. â€œWeâ€™re producing our crops at a loss now, just like the oil guys are pumping oil at a loss,â€ Mr. Halcomb, who grows corn, soybeans, wheat and barley on his   family farm, said by telephone on Wednesday. â€œYou canâ€™t cut your costs fast enough. â€ It is a common plight of farmers across the United States, with the global agriculture industry in a wrenching downturn. Because farmers have produced too much corn, wheat and soybeans, they have been forced to slash prices to sell their crops. They have also reduced spending on seeds, pesticides and fertilizer, which has eaten into sales at agribusiness giants, including Monsanto and DuPont. In response, these companies have sought   deals to cut costs and weather the industryâ€™s storm. Four major agribusiness mergers have been announced in the last year. The latest is Bayer AGâ€™s $56 billion takeover of Monsanto  â€”   the largest acquisition of 2016  â€”   announced on Wednesday. Every merger creates the possibility of higher costs for farmers. Mr. Halcomb buys seeds with traits licensed to Monsanto of St. Louis and seeds from DuPont, which has a deal pending to merge with Dow Chemical. His fertilizers are made of potassium compounds and phosphate produced by Agrium of Calgary, Alberta, which on Monday agreed to combine with the fertilizer producer Potash Corporation of Saskatchewan. He uses pesticides made by Syngenta of Switzerland, which agreed in February to a takeover by the China National Chemical Corporation. â€œItâ€™s just like any other industry that consolidates,â€ Mr. Halcomb said. â€œThey tell the regulators theyâ€™re   and then they tell their customers they have to increase pricing after the dealâ€™s done. â€ The companies say they are merging to diversify and increase growth and research capabilities, but these deals, given their size and scope, have already caught the attention of lawmakers and regulators in Washington. There is no guarantee that they will all receive regulatory approval, and some companies may have to sell assets to allay antitrust concerns. Dowâ€™s merger with DuPont is under Justice Department review. The market seemed to anticipate hurdles for the Monsanto deal on Wednesday. Shares of the company closed about 20 percent lower than the $128 per share cash offer from Bayer, which is based in Leverkusen, Germany. Shares of each company gained less than 1 percent after the deal was announced. Adding the assumption of about $10 billion of Monsanto debt, Bayerâ€™s total $66 billion pact is the largest   deal, according to data compiled by Thomson Reuters, ahead of InBevâ€™s $60. 4 billion offer for another St.   company,   in June 2008. Senator Charles E. Grassley, Republican of Iowa and chairman of the Judiciary Committee, scheduled a hearing next week to discuss the possible effect of these   mergers on farming. Iowa produced more corn last year than any other state, according to the National Corn Growers Association. â€œIt seems to be catching fire and happening so fast with so many,â€ Senator Grassley said in a phone interview. â€œWhen you have less competition, prices go up. â€ European competition regulators also said publicly, before a   deal was even signed, that they would look at how it could affect prices and the availability of seed products, as well as research. Liam Condon, who leads Bayerâ€™s   division, said in an interview that the company did an â€œextensive analysisâ€ with regard to antitrust before approaching Monsanto in May. Mr. Condon said that he does not believe there is much overlap between their portfolios, because Bayerâ€™s focus is largely on crop protection, while Monsantoâ€™s is on seeds and traits. He said the companies assume they may need to sell off some assets to appease regulators. Monsanto, which is famous for its production of genetically modified seeds, rejected several offers from Bayer as too low. Wednesdayâ€™s deal represented a 44 percent premium to Monsantoâ€™s stock price on May 9, the day before Bayerâ€™s interest in a deal surfaced. To assuage Monsantoâ€™s concerns, Bayer threw in a $2 billion breakup fee if the deal fell apart on antitrust grounds. The strategic goal of the deal, according to Bill Selesky, an analyst at Argus Research, is to create a    experience for farmers, making Bayer the worldâ€™s largest supplier of seeds and farm chemicals. By improving the product for farmers, the combined company could ultimately raise prices, Mr. Selesky said in an interview. Senator Grassley said that he had spoken with a few farmers who believed the deals were necessary so large agribusinesses could continue to absorb the costs of researching and developing products and getting government approval for them. Bayer and Monsanto said they planned to cut about $1. 2 billion worth of costs as part of the deal, helping to improve efficiency. But Jim Benham of Versailles, Ind. the president of the Indiana Farmers Union, was not so optimistic. He blamed the rising costs of inputs  â€”   seeds, fertilizer and the like  â€”   for eating away at farmersâ€™ profit margins, and warned that consolidation will make it worse. Costs have already risen by double digits over the last four to five years, and the proposed   merger could accelerate that. â€œThe merger is going to hurt the farmer,â€ said Mr. Benham, who grows corn, soybeans and sometimes wheat on his   farm. â€œThe more consolidation we have on our inputs, the worse it gets. â€ Mr. Condon of Bayer said that the company would not raise prices without providing more value to farmers. â€œThis is a highly competitive industry, and just increasing prices without having any additional advantage or benefit for growers wonâ€™t go anywhere,â€ he said. â€œItâ€™s up to us to show what weâ€™re offering will help farmers improve their return on investment. â€ Some farmers said the consolidation could even enable prices to fall. Christine Hamilton manages a farm of more than 12, 000 acres in Kimball, S. D. growing crops like corn and operating a ranch. She said that if the deal can pass the antitrust screening, then maybe it could actually help farmers. â€œI understand how companies need to get bigger in order to be competitive,â€ she said. â€œAs we are in a low part of the cycle, anything that might have a chance of reducing our input prices would be great. â€")#LOAD MODEL
loaded_vec = CountVectorizer(vocabulary=pickle.load(open("count_vector_type.pkl", "rb")))
loaded_tfidf = pickle.load(open("tfidf_type.pkl","rb"))
loaded_model = pickle.load(open("nb_model_type.pkl","rb"))

X_new_counts = loaded_vec.transform(docs_new)
X_new_tfidf = loaded_tfidf.transform(X_new_counts)
predicted = loaded_model.predict(X_new_tfidf)

print(category_list[predicted[0]])