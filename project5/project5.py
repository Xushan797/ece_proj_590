"""
Math 560
Project 5
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####
    # Initialize all costs to +infinity and prev to null
    for vertex in adjList:
        vertex.cost = +float('inf')
        vertex.prev = None
    # pick the first node to start
    adjList[0].cost = 0
    #Make the priority queue using cost for sorting
    queue = PriorityQueue(adjList)
    while not queue.isEmpty():
        #Get the next unvisited vertex and visit it
        v = queue.deleteMin()
        v.visited = True
        #For each edge out of v
        for neighbor in v.neigh:
            #If the edge leads out, update
            if not neighbor.visited:
                if neighbor.cost > adjMat[v.rank][neighbor.rank]:
                    neighbor.cost = adjMat[v.rank][neighbor.rank]
                    neighbor.prev = v

    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    # Initialize all singleton sets for each vertex
    for vertex in adjList:
        makeset(vertex)
    # Initialize the empty MST
    X = []
    # Loop through the edges in increasing order
    for e in edgeList:
        # If the min edge crosses a cut, add it to our MST
        u, v = e.vertices[0], e.vertices[1]
        if  not find(u).isEqual(find(v)):
            X.append(e)
            union(u,v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    ##### Your implementation goes here. #####
    #construction of the union find
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    ##### Your implementation goes here. #####
    #If we are not at the root
    while v != v.pi:
        #Set our parent to be the root
        #which is also the root of our parent
        v = find(v.pi)
    # Return the root, which is now our parent
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    ##### Your implementation goes here. #####
    #First, find the root of the tree for u
    #and the tree for v
    ru = find(u)
    rv = find(v)
    # If the sets are already the same, return
    if ru == rv:
        return
    # Make shorter set point to taller set
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        # Same height, break tie
        ru.pi = rv
        # Tree got taller, increment rv.height
        rv.height += 1
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    # Initialize all the vertex in adjList to be not visited
    for vertex in adjList:
        vertex.visited = False
    #travelling salesman problem solution
    ##### Your implementation goes here. #####
    tour = []
    stack = [start]
    # We use the dfs method,stack to find the tour path
    while stack:
        #pop node in stack
        node = stack.pop()
        #set node to be visited
        node.visited = True
        #append in the tour path
        tour.append(node.rank)
        for vertex in node.mstN:
            #add all other not visited vertex in the adjent mstN in the list
            if not vertex.visited:
                stack.append(vertex)
    # Finally, add the start node at the end of the tour to be a circle
    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
