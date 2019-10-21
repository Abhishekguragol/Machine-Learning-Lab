import pandas as pd
import math

class DT:
    def __init__(self,split,value=[]):
        self.split = split #value_for_node
        self.values = value#value_for_child
        
df = pd.read_csv('data3.csv')

def findbestsplit(Ex,Attr):
    best=10
    split = None
    for cond in Attr:
        if cond == 'Play Tennis':
                continue
        ent = calentropy(cond,Ex)
        if ent < best:
            best = ent
            split = cond
    return split

def calentropy(cond,data):
    values = data[cond].unique()
    #cond is col, data is df
    tot = data.shape[0]
    total_ent = 0
    for i in values:
        weight = len(data.loc[data[cond]==i])
        yc = list(data.loc[data[cond]==i][data.columns[-1]]).count('Y')
        nc = weight - yc
        if yc == 0:
                pos = 0
        else:
                pos = abs(math.log2(yc/weight))
        if nc == 0:
                neg = 0
        else:
                neg = abs(math.log2(nc/weight))
        total_ent+=(weight/tot)*(pos+neg)
    return total_ent

def removeattr(Attributes,split_attr):
        l = []
        for i in Attributes:
                if i!=split_attr:
                        l.append(i)
        return l

def ID3(Ex,Attributes):
        unique = Ex[Ex.columns[-1]].unique()
        if len(unique) == 1:
                if 'N' in unique:
                        return(DT('no',[]))
                else:
                        return(DT('yes',[]))  
        if len(Attributes)==1:
                cp = list(Ex[Ex.columns[-1]]).count('Y')
                np = list(Ex[Ex.columns[-1]]).count('N')
                if cp>np:
                         return(DT('yes',[]))
                else:
                        return(DT('no',[]))
        split_attr = findbestsplit(Ex,Attributes)
        node = DT(split_attr)
        vals = Ex[split_attr].unique()
        l = []
        for i in vals:
                Exi = Ex.loc[Ex[split_attr] == i]
                if len(Exi) == 0:
                        cp = list(Ex[Ex.columns[-1]]).count('Y')
                        np = list(Ex[Ex.columns[-1]]).count('N')
                        if cp>np:
                                child = DT('yes',[])
                        else:
                                child = DT('no',[])
                        l.append([i,child])
                else:
                        Child_Attr = removeattr(Attributes,split_attr)
                        l.append([i,ID3(Exi,Child_Attr)])
                        node.values = l[:]
        return node
        
attributes = list(df.columns[:])
root = ID3(df,attributes)

def print_node(node,n):
    if(node.split=='yes' or node.split=='no'):
        print("\t"*n,node.split)
    else:
        print("\t"*n,node.split+":")
    for i in node.values:
        print("\t"*(n+1),i[0]+":")
        print_node(i[1],n+2)
        print()
print_node(root,0)