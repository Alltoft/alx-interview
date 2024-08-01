#!/usr/bin/python3
"""a script that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """this function returns the perimeter of the island described in grid"""

    perim = 0
    rown = 0
    try:
        for row in grid:
            coln = 0
            for column in row:
                if column == 0:
                    pass
                else:
                    if grid[rown-1][coln] == 0:
                        perim += 1
                    if grid[rown][coln-1] == 0:
                        perim += 1
                    if grid[rown][coln+1] == 0:
                        perim += 1
                    if grid[rown+1][coln] == 0:
                        perim += 1
                coln += 1
            rown += 1
    except IndexError:
        Value = 0

    return perim