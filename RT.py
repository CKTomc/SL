#data is an iterable object
#features_values is a dict of feature:[<values>]
#getfeatures operates by verifying which valid features to select for the next step
from random import randrange

class node():
    def __init__(self):
        self.feature=None
        self.value=None
        self.position=None
        self.leftchild=None
        self.rightchild=None
        self.outputleft=None
        self.outputright=None

def newtree(data,features,features_values,head,depth,d,target,categorical_features):      
        loss=10000000000000
        for f in features:
            for v in features_values[f]:
                sumyinf=0
                sumysup=0
                yinf=[]
                ysup=[]
                for i in data:
                    if (categorical_features.get(f)==None and i[features_subset[f]]<=v)or (categorical_features.get(f)!=None and i[features_subset[f]]==v):
                        sumyinf+=i[target]
                        yinf.append(i[target])
                    elif (categorical_features.get(f)==None and i[features_subset[f]]>v)or (categorical_features.get(f)!=None and i[features_subset[f]]!=v):
                        sumysup+=i[target]
                        ysup.append(i[target])
                        
                if len(yinf)!=0 and len(ysup)!=0:
                   binf=sumyinf/len(yinf)                  
                   bsup=sumysup/len(ysup)                     
                   squared_loss=sum((y-binf)**2 for y in yinf)+sum((y-bsup)**2 for y in ysup)
                   if squared_loss<loss:
                     loss=squared_loss
                     feature=f
                     value=v               
        
        head.feature=feature
        head.position=features.index(feature)
        head.value=value
        d+=1           
        
        if categorical_features.get(feature)!=None: 
           dataleft=[d for d in data if d[features_subset[feature]]==value]
           dataright=[d for d in data if d[features_subset[feature]]!=value]
           features_values_right=get_features_values(dataright,features)
           features_values_left=get_features_values(dataleft,features)
           del(features_values_left[feature])
           
        else:
           dataleft=[d for d in data if d[features_subset[feature]]<=value]
           dataright=[d for d in data if d[features_subset[feature]]>value] 
           features_values_right=get_features_values(dataright,features)
           features_values_left=get_features_values(dataleft,features)
           features_values_left[feature].remove(value)
           
        if d<depth :   
               features_left=getfeatures(features,features_values_left)       
               features_right=getfeatures(features,features_values_right)            
                             
               if features_left!=[] and features_right!=[]:
                   head.leftchild=node()
                   head.rightchild=node() 
                   newtree(dataleft,features_left,features_values_left,head.leftchild,depth,d,target,categorical_features)              
                   newtree(dataright,features_right,features_values_right,head.rightchild,depth,d,target,categorical_features)
                
               elif features_left==[] and features_right!=[] :
                   head.outputleft=sum(ins[target] for ins in dataleft)/len(dataleft)
                   head.rightchild=node()
                   newtree(dataright,features_right,features_values_right,head.rightchild,depth,d,target,categorical_features)
                   
               elif features_left!=[] and features_right==[]:
                   head.outputright=sum(ins[target] for ins in dataright)/len(dataright)
                   head.leftchild=node()
                   newtree(dataleft,features_left,features_values_left,head.leftchild,depth,d,target,categorical_features)              
               
               else:
                    head.outputleft=sum(ins[target] for ins in dataleft)/len(dataleft)
                    head.outputright=sum(ins[target] for ins in dataright)/len(dataright)
          
            
        else:
                head.outputleft=sum(ins[target] for ins in dataleft)/len(dataleft)
                head.outputright=sum(ins[target] for ins in dataright)/len(dataright)
   

def prediction(instance,head,categorical_features):
    if instance[head.position]==head.value:
        if head.leftchild!=None:
            return prediction(instance,head.leftchild,categorical_features)
        else:
            return head.outputleft
    else:
        if categorical_features.get(head.feature)!=None or (categorical_features.get(head.feature)==None and instance[head.position]>head.value): 
           if head.rightchild!=None:
              return prediction(instance,head.rightchild,categorical_features)
           else:
              return head.outputright
        if categorical_features.get(head.feature)==None and instance[head.position]<head.value:        
            if head.leftchild!=None:
                return prediction(instance,head.leftchild,categorical_features)
            else: 
                return head.outputleft
    
/*create*/
tree=node()
newtree(data,features,features_values,tree,depth,d,target,categorical_features)
/*test*/
testpoint=data[randrange(len(data))]
predicted=prediction(instance,tree)
print("target:",testpoint[target],",prediction:',predicted")
