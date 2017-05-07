#Uses python2

import sys
from collections import defaultdict
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
#Uses python2

import sys

#visit=dict()
#topo=[]

#topo=myStack()
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
def distance(Graph,s,t,a,b):
    q=Queue()
    dist=[a+1]*(b+1)
    
    dist[s]=0
    q.enqueue(s)
    while(not q.isEmpty()):
        u=q.dequeue()
       
        for k in Graph.graph[u]:
            if dist[k]==a+1:
                q.enqueue(k)
                dist[k]=dist[u]+1
    if dist[t]==a+1:
        print -1
    else:
        print dist[t]
            
def isBipartiteU(Graph,s,color):
    color[s]=1
    q=Queue()
    q.enqueue(s)
    while(not q.isEmpty()):
        u=q.dequeue()
        for k in Graph.graph[u]:
            if color[k]==-1:
                color[k]=1-color[u]
                q.enqueue(k)
            elif color[k]==color[u]:
                return False
    return True
          
    #return path
    #for node in Graph.vertList[start].getConnections():
        #if not node in path:
            #print node.getId()
            #path=reach(Graph, node.getId(), path)
    #return path


def isBipartite(Graph,a):
    color=[-1]*(a+2)
    for i in xrange(1,a+2):
        if color[i]==-1:
            if(isBipartiteU(Graph,i,color)==False):
                return False
    return True
    
if __name__ == '__main__':
    i=0
    j=0
    k=0
    l=0
    r=1
    q=1
    c=[]
    o=[]
    
    
    input1 = raw_input()
    data = input1.split()
    for i in xrange(len(data)):
        data[i]=int(data[i])
    m=data[0]
    g=Graph(m+1)
    n=data[1]
   
    for j in xrange(0,n):
        input2=raw_input()
        data1=input2.split()
        for k in xrange(len(data1)):
            data1[k]=int(data1[k])
        g.addEdge(data1[0],data1[1])
        g.addEdge(data1[1],data1[0])

    #input3=raw_input()
    #data2=input3.split()
    #for l in xrange(len(data2)):
        #data2[l]=int(data2[l])
    #distance(g,data2[0],data2[1],n,m+1)
    if isBipartite(g,m+1):
        print 1
    else:
        print 0
    
    #topo.reverse()
    #for i in xrange(len(topo)):
        #print topo[i],
