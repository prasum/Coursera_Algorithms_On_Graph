#Uses python2

import sys
sys.setrecursionlimit(200000)



from collections import defaultdict
  
#This class represents a directed graph using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
  
    # A function used by DFS
    def DFSUtil(self,v,visited):
        # Mark the current node as visited and print it
        visited[v]= True
        #print v,
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
 
 
    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited 
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
     
 
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
 
  
  
    # The main function that finds and prints all strongly
    # connected components
    def printSCCs(self):
        count=0
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
 
        # Create a reversed graph
        gr = self.getTranspose()
         
        # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)
 
        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSUtil(i, visited)
                count=count+1
        print count
        

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
g=Graph(m)
n=data[1]
for j in xrange(0,n):
    input2=raw_input()
    data1=input2.split()
    for k in xrange(len(data1)):
        data1[k]=int(data1[k])
        data1[k]=data1[k]-1
    g.addEdge(data1[0],data1[1])
g.printSCCs()