# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:03:48 2021

@author: 
    Computing connected component using breath first search
    
  
"""

from collections import defaultdict
class UCC:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def Ucc(self):
        
        visited = []
        numUcc = 0
        
        queue = []
        cc = []
        
        for i in self.graph.keys():
            if i not in visited:
                numUcc = numUcc + 1
                queue.append(i)
                
                while queue:
                    v = queue.pop(0)
                    if (v, numUcc) not in cc:
                        
                        cc.append((v, numUcc))
                    for j in self.graph[v]:
                        if j not in visited :
                            visited.append(j) 
                            queue.append(j)
        return cc                 
        
g = UCC()
g.addEdge(1, 5)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(3, 1)
g.addEdge(3, 5)
g.addEdge(4, 2)
g.addEdge(5, 7)
g.addEdge(5, 9)
g.addEdge(5, 3)
g.addEdge(5, 1)
g.addEdge(6, 8)
g.addEdge(6, 10)
g.addEdge(7, 5)
g.addEdge(8, 6)
g.addEdge(9, 5)
g.addEdge(10, 6)
print(g.Ucc())
