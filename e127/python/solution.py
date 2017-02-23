# Definition for a Directed graph node
:%s
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        self.solid = {}
        for node in graph:
            self.calcOrder(node, graph)
        func = lambda node: self.solid[node]
        return sorted(self.solid, key=func, reverse=True)      
        
    def calcOrder(self, node, graph):    
        if not node.neighbors:
            self.solid[node] = 0
            return 0
        elif self.solid.has_key(node):
            return self.solid[node]
        else:
            nb_orders = [self.calcOrder(n, graph) for n in node.neighbors]
            order = max(nb_orders) + 1
            self.solid[node] = order
            return order
  
