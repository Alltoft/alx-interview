#!/usr/bin/python3
"""A script that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """This function returns the perimeter of the island described in grid"""
    perim = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row-1][col] == 0:
                    perim += 1
                if col == 0 or grid[row][col-1] == 0:
                    perim += 1
                if col == cols-1 or grid[row][col+1] == 0:
                    perim += 1
                if row == rows-1 or grid[row+1][col] == 0:
                    perim += 1

    return perim
