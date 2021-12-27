"""
Math 560
Project 4
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')
    m = len(src)
    n = len(dest)
    match_matrix = [[0] * (n+1) for _ in range(m+1)]
    if prob == 'ED':
        for i in range(n+1):
            match_matrix[0][i] = i
    for i in range(m+1):
        match_matrix[i][0] = i
    for i in range(1,m+1):
        for j in range(1,n+1):
            if src[i-1] == dest[j-1]:
                match_matrix[i][j] = match_matrix[i-1][j-1]
            else:
                match_matrix[i][j] = 1 + min(match_matrix[i][j-1],match_matrix[i-1][j],match_matrix[i-1][j-1])
    dist = match_matrix[m][n] # This is a placeholder, remove and implement!
    i = m
    j = n
    edits = []
    while i>0 or j>0:
        if i == 0 and j>0:
            edits.append(('insert', dest[j-1], 0))
            j -= 1
        elif i >0 and j == 0:
            edits.append(('delete', src[i-1], i-1))
            i -= 1
        else:
            if src[i-1] == dest[j-1]:
                edits.append(('match', src[i - 1], i - 1))
                i -= 1
                j -= 1
            else:
                if match_matrix[i][j] == match_matrix[i-1][j-1] + 1:
                    edits.append(('sub', dest[j - 1], i - 1))
                    i -= 1
                    j -= 1
                elif match_matrix[i][j] == match_matrix[i][j-1] + 1:
                    edits.append(('insert', dest[j-1], i))
                    j -= 1
                elif match_matrix[i][j] == match_matrix[i-1][j] + 1:
                    edits.append(('delete', src[i - 1], i - 1))
                    i -= 1

    # This is a placeholder, remove and implement!
    #print(src,dest,edits,dist)
    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
