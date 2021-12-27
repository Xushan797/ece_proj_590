"""
Math 560
Project 3
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    print(adjList)
    print(adjMat)
    n = len(adjList)
    adjList[0].dist = 0
    for k in range(n-1):
        for node in adjList:
            for neigh in node.neigh:
                if neigh.dist > node.dist + adjMat[node.rank][neigh.rank] + tol:
                    neigh.dist = node.dist + adjMat[node.rank][neigh.rank]
                    neigh.prev = node
    flag = 0
    curnode = None
    for node in adjList:
        for neigh in node.neigh:
            if neigh.dist > node.dist + adjMat[node.rank][neigh.rank] + tol:
                neigh.dist = node.dist + adjMat[node.rank][neigh.rank]
                neigh.prev = node
                flag = 1
                curnode = neigh
                break
        if flag == 1:
            break
    if flag == 0:
        return []
    path = [curnode.rank]
    start = None
    while curnode.prev:
        if curnode.prev.rank in path:
            start = curnode.prev.rank
            path.append(curnode.prev.rank)
            break
        path.append(curnode.prev.rank)
        curnode = curnode.prev
    index = 0

    for i in range(len(path)):
        if path[i] == start:
            index = i
            break
    print(reversed(path[index:]))
    return list(reversed(path[index:]))

    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.

    return ([[math.log(1/R) for R in row] for row in rates])

    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
