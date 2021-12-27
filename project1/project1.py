"""
Math 560
Project 1
Fall 2021

Partner 1:
Partner 2:
Date:
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    n = len(listToSort)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if listToSort[j] < listToSort[min_index]:
                min_index = j
        listToSort[i], listToSort[min_index] = listToSort[min_index], listToSort[i]
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    n = len(listToSort)
    for i in range(n):
        for j in range(i,0,-1):
            if listToSort[j] < listToSort[j-1]:
                listToSort[j],listToSort[j-1] = listToSort[j-1],listToSort[j]
            else:
                break
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    n = len(listToSort)
    for i in range(n):
        flag = 0
        for j in range(n-i-1):
            if listToSort[j] > listToSort[j+1]:
                listToSort[j +1],listToSort[j] = listToSort[j],listToSort[j+1]
                flag = 1
        if flag == 0:
            break

    return listToSort

"""
MergeSort
"""

import copy
def MergeSort(listToSort):
    def merge(l, mid, r):
        leftlist = copy.deepcopy(listToSort[l:mid+1])
        rightlist = copy.deepcopy(listToSort[mid+1:r+1])
        i, j = 0, 0
        index = l
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] <= rightlist[j]:
                listToSort[index] = leftlist[i]
                i += 1
            else:
                listToSort[index] = rightlist[j]
                j += 1
            index += 1
        while i < len(leftlist):
            listToSort[index] = leftlist[i]
            i += 1
            index += 1
        while j < len(rightlist):
            listToSort[index] = rightlist[j]
            j += 1
            index += 1
    def mergesortHelper(l, r):
        if l<r:
            mid = (l + r) // 2
            mergesortHelper( l, mid)
            mergesortHelper(mid + 1, r)
            merge( l, mid, r)
    n = len(listToSort)
    mergesortHelper( 0, n - 1)
    return listToSort

"""
QuickSort


Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    #Set default value for j if None.
    if j == None:
        j = len(listToSort)
    index = i
    x = i
    y = j-1
    if x<y:
        while (x < y):
            #print(x,y,len(listToSort))
            while x<y and listToSort[y] >= listToSort[index]:
                y -= 1
            while x<y and listToSort[x] <= listToSort[index]:
                x += 1
            listToSort[x],listToSort[y] = listToSort[y],listToSort[x]
        listToSort[x],listToSort[index] = listToSort[index],listToSort[x]
        QuickSort(listToSort,i,x)
        QuickSort(listToSort,x+1,j)
    return listToSort





"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime()
