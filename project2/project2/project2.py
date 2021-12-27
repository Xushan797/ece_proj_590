#-*-coding:utf-8-*-
"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1:
Partner 2:
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.

    print(maze.exit.rank)
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    def dfs():
        curr = None
        stack = Stack()
        #starting from the start Vertex
        stack.push(maze.start)
        maze.start.visited = True
        while not stack.isEmpty():
            curr = stack.pop()
            print(curr.rank)
            # if we arrive at the end vertex, we solve the maze, break
            if curr.isEqual(maze.exit):
                break
            # use dfs to detect neighbor
            for node in curr.neigh:
                if not node.visited:
                    node.visited = True
                    node.prev = curr
                    stack.push(node)
        path = []
        while curr:
            path.append(curr.rank)
            curr = curr.prev
        maze.path = path[::-1]
        return maze.path
    if alg == 'DFS':
        return dfs()
    ##### Your implementation goes here. #####
    return []

    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":

    testMazes(False)