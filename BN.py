from sklearn.naive_bayes import GaussianNB
import random
global output_ind
global data
global output
global test

output_ind= the index of the output
<intialize the data>
output=[x[output_ind] for x in data]
data=[x[:-1] for x in data]
<initialize test data>

gnb = GaussianNB()
classifier = gnb.fit(data,output)
testpoint=random.choice(test)
prediction=classifier.predict(testpoint)
print(testpoint,prediction)
