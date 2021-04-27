import numpy as np
import random
from sklearn import svm
global output_ind
global data
global output

output_ind= the index of the output
<intialize the data>
output=[x[output_ind] for x in data]
data=[x[:-1] for x in data]

X_train , X_test , y_train, y_test = train_test_split(data, output, random_state=0)
clf = svm.SVC(kernel='precomputed')
gram_train = np.dot(X_train, X_train.T)
clf.fit(gram_train, y_train)

gram_test = np.dot(X_test, X_train.T)
clf.predict(gram_test)
