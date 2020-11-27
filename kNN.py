global output_ind
global data
output_ind= the index of the output
<intialize the data>

def kNN(element,k): 
    nearest=set()   
    for d in data:
      if d!=instance:
        dist=distance(d,i) # using a distance measure (ex : Manhattan)
        nearest.add((dist,d))
    nearest=list(nearest)
    nearest=[nearest[neighbour][1] for neighbour in range(k)]
    #now for the estimation, which is not always requiered
    estimation= sum(neighbour[output_ind] for neighbour in nearest)
    return nearest,estimation
