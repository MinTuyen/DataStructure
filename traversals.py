
# Iterates over a 2D list from left to right, then top to bottom
# and returning the coordinates (row, column).
def row_major_traversal (grid):
    """traversal row"""
    rows=len(grid)
    cols=len(grid[0])
    result = []
    for r in range(rows):
        for c in range(cols):
            result.append((r,c))
    return result
# Iterates over a 2D list from left to right, then top to bottom
# and returning the coordinates (row, column).
def column_major_traversal (grid):
    """traversal column"""
    rows=len(grid)
    cols=len(grid[0])
    result = []
    for c in range (cols):
        for r in range(rows):
            result.append((r,c))
    return result
# Iterates over a 2D list from top to bottom then left to right
# and returning the coordinates (row, column).
def row_zigzag_traversal (grid):
    """traversal row zigzag"""
    rows = len(grid)
    cols = len(grid[0])
    result = []
    for r in range(rows):
        if r % 2 == 1:
            for c in range(cols-1, -1, -1):
                result.append((r, c))
        else:
            for c in range(cols):
                result.append((r, c))
    return result
# Iterates over a 2D list by alternating between iterating
# left to right and right to left, going from top to bottom
# and returning the coordinates (row, column).
def column_zigzag_traversal (grid):
    """traversal column zigzag"""
    rows = len(grid)
    cols = len(grid[0])
    result = []
    for c in range(cols):
        if c % 2 == 1:
            for r in range(rows-1, -1, -1):
                if 0 <= r < rows:
                    result.append((r, c))
        else:
            for r in range(rows):
                if 0 <= r < rows:
                    result.append((r, c))
    return result
# Iterates over a 2D list from the top-right to the bottom-left
# in the direction of the main diagonal and returning the
# coordinates (row, column).
def main_diagonal_traversal (grid):
    """traversal main diagonal"""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    result = []
    for k in range(rows + cols - 1):
        for r in range(max(0, k - cols + 1), min(k, rows - 1) + 1):
            c = k - r
            if 0 <= r < rows and 0 <= c < cols:
                result.append((r, cols - 1 - c))

    return result
# Iterates over a 2D list from the top-left to the bottom-right
# in the direction of the secondary diagonal and returning the
# coordinates (row, column).
def secondary_diagonal_traversal (grid):
    """traversal secondary diagonal"""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    result = []
    for k in range(rows + cols - 1):
        for r in range(max(0, k - cols + 1), min(k, rows - 1) + 1):
            c = k - r
            if 0 <= r < rows and 0 <= c < cols:
                result.append((r, c))
    return result
# Iterates over a 2D list in spiral order and returning the
# coordinates (row, column).
def spiral_traversal (grid):
    """traversal spiral"""
    row1 = 0
    row2 = len(grid) - 1
    col1 = 0
    col2 = len(grid[0]) - 1
    result = []
    while row1 <= row2 and col1 <= col2:
        for c in range(col1, col2 + 1):
            result.append((row1, c))
        for r in range(row1 + 1, row2 + 1):
            result.append((r, col2))
        if row1 < row2:
            for c in range(col2 - 1, col1 - 1, -1):
                result.append((row2, c))
        if col1 < col2:
            for r in range(row2 - 1, row1, -1):
                result.append((r, col1))
        row1 += 1
        row2 -= 1
        col1 += 1
        col2 -= 1
    return result
