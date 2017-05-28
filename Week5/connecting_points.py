#Uses python2

import math

Parent=[]
Rank=[]
x=[]
y=[]
p=[]
def find1(l,ele):
    for row,i in enumerate(l):
        try:
            col=i.index(ele)
        except ValueError:
            continue
        return row
    return -1,-1

def EdgeMatrix(n):
    Edge=[[0]*n]*n
    return Edge


def MakeSet(n):
    for i in xrange(n):
        Parent.append(i)
        Rank.append(0)
    

def distance(a,b):
    u=len(a)
    k=EdgeMatrix(u)
    for i in xrange(u):
        for j in xrange((i+1),u):
            r=math.sqrt(((x[i]-x[j])*(x[i]-x[j]))+((y[i]-y[j])*(y[i]-y[j])))
            #print r
            p.append([i,j,r])
    
    


    
def find(item):
    #print "Parent"+Parent
    if Parent[item]==item:
        return item
    return find(Parent[item])
        
def union(item1,item2):
    xroot = find(item1)
    yroot = find(item2)
    if xroot!=yroot:
        
        if Rank[xroot]>Rank[yroot]:
            Parent[yroot]=xroot
        else:
            Parent[xroot]=yroot
            if Rank[xroot]==Rank[yroot]:
                Rank[yroot]=Rank[yroot]+1
        
def kruskal():
    e=[]
    s=0
    a=len(x)
    MakeSet(a)
    c=[]
    q=[]
    distance(x,y)
    #temp=distance(x,y)
    b=tuple()
    p.sort(key = lambda p : p[2])
    #print p
    for m in xrange(len(p)):
   
        u=p[m][0]
        v=p[m][1]
                
       
        #print u,v
        if find(u)!=find(v):
                        b=(u,v) 
                        #print find(u),find(v)
                        q.append(b)
                        s=s+p[m][2]
                        union(u,v)
        #p[m][2]=0.0
    #print q
    return s
            
    
    
        










m=input()
for i in range(int(m)):
    k=raw_input()
    l=k.split()
    for g in xrange(len(l)):
        l[g]=int(l[g])
    x.append(l[0])
    y.append(l[1])
#distance(x,y)
print '%.9f' % kruskal()

