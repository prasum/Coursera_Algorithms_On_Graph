
#Uses python2

import sys
s=[]
flag=0
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

#def reach(adj, x, y):
    #write your code here
    #return 0
def reach(Graph, start, path=[]):
    path=path+[start]
    #visit[start]=1
    #s.append(start)
    #print Graph.vertList
    #start=Graph.getVertex(start):
    for j in Graph.vertList.values():
        if j.getId()==start:
            #visit[j.getId()]=1
            #s.append(j.getId())
            for u in j.getConnections():
                #k.append(u.getId())
                #if u.getId() in s:
                    #return 1
                if  u.getId() in path:
                    return True
                else: 
					if reach(g,u.getId(),path):
						return True
    path.remove(start)
    return False
                
                
    #for node in Graph.vertList[start].getConnections():
        #if not node in path:
            #print node.getId()
            #path=reach(Graph, node.getId(), path)
    #return path

def cycle(Graph):
    flag=0
    for i in Graph.vertList.values():
        k=i.getId()
        y=reach(Graph,k)
        if y==True:
            flag=1
            break
    if flag==1:
        print 1
    else:
        print 0
if __name__ == '__main__':
    i=0
    j=0
    k=0
    l=0
    r=1
    q=1
    c=[]
    o=[]
    g=Graph()
    input1 = raw_input()
    data = input1.split()
    for i in xrange(len(data)):
        data[i]=int(data[i])
    m=data[0]
    for q in xrange(1,m+1):
        g.addVertex(q)
    n=data[1]
    for j in xrange(0,n):
        input2=raw_input()
        data1=input2.split()
        for k in xrange(len(data1)):
            data1[k]=int(data1[k])
        g.addEdge(data1[0],data1[1],0)
        #g.addEdge(data1[1],data1[0],0)
    cycle(g)
   
    #input3=raw_input()
    #data2=input3.split()
    #for l in xrange(len(data2)):
        #data2[l]=int(data2[l])
    #o=reach(g,data2[0],c)
    #if data2[1] in o:
        #print 1
    #else:
        #print 0
    #for r in g.vertList.values():
        #for s in r.getConnections():
            #print r.getId(),s.getId()




