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
           features_values_right=get_features_values(dataright,target,features)
           features_values_left=get_features_values(dataleft,target,features)
           del(features_values_left[feature])
           
        else:
           dataleft=[d for d in data if d[features_subset[feature]]<=value]
           dataright=[d for d in data if d[features_subset[feature]]>value] 
           features_values_right=get_features_values(dataright,target,features)
           features_values_left=get_features_values(dataleft,target,features)
           features_values_left[feature].remove(value)
           
        if d<depth :           
   
