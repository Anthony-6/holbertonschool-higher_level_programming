#!/usr/bin/python3
'''
-Create a function def pascal_triangle(n): that returns a
 list of lists of integers representing the Pascal’s triangle of n:
-Returns an empty list if n <= 0
-You can assume n will be always an integer
'''


def pascal_triangle(n):
    '''
    this function return a list of integer represented by
    the pascal's triangle
    '''
    if n <= 0:
        return []
    List = [[]]
    Val = 0
    for i in range(n):
        addStart = 0
        addEnd = 0
        List[i].append(1)
        if i >= 2:
            for j in range(Val):
                List[i].append(List[i - 1][addStart] + List[i - 1][addEnd + 1])
                addStart += 1
                addEnd += 1
        if i >= 1:
            List[i].append(1)
            Val += 1
        if i != n - 1:
            List.append([])
    return List
