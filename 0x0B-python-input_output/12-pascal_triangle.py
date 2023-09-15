#!/usr/bin/python3
""" function that returns a list of lists of integers """


def pascal_triangle(n):
    """ returns pascal_triangle """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        previous_row = triangle[-1]
        new_rpw = [1]
        for j in range(1, i):
            new_element = previous_row[j - 1] + previous_row[j]
            new_row.append(new_element)

        new_row.append(1)  # The last element is always 1
        triangle.append(new_row)
