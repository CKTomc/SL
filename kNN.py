global output_ind
global data
output_ind= the index of the output
<intialize the data>

def kNN(element,k): 
    nearest=set()   
    for d in data:
      if d!=instance:
        dist=distance(d,i) # ex Manhattan
        nearest.add((dist,d))
    #nearest=list(nearest)
    nearest=[nearest[neighbour][1] for neighbour in range(k)]
    #now for the estimation, which is not always required
    estimation= sum(neighbour[output_ind] for neighbour in nearest)/len(nearest)
    return nearest,estimation

*************using sklearn: example **************
import random
from sklearn.neighbors import KNeighborsClassifier

global output_ind
global data
global output
output_ind= the index of the output
<intialize the data>
output=[x[output_ind] for x in data]
data=[x[:-1] for x in data]

#training
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(data,output)

#prediction
print(classifier.predict(random.choice(data)))
print(classifier.predict_proba(random.choice(data)))

#neighbours
from sklearn.neighbors import NearestNeighbors
neighbourhood=NearestNeighbors(n_neighbors=5)
neighbourhood.fit(data)
print(neighbourhood.kneighbors(random.choice(data))) # returns distances with neighbours inds
