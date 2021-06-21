def sudoku2(grid):
    quad1, quad2, quad3 = [0, 1, 2], [3, 4, 5], [6, 7, 8]

    for i in range(len(grid)):
        for j, val in enumerate(grid[i]):
            if val != ".":
                # check row
                rowCount = 0
                for num in grid[i]:
                    if num == val:
                        rowCount += 1
                if rowCount > 1:
                    return False

                # check column
                colCount = 0
                for row in range(len(grid)):
                    if grid[row][j] == val:
                        colCount += 1
                if colCount > 1:
                    return False
                    
                # check quadrant
                quadCount = 0
                quadi = []
                quadj = []
                if i == 0 or i == 1 or i == 2:
                    quadi = quad1
                elif i == 3 or i == 4 or i == 5:
                    quadi = quad2
                else:
                    quadi = quad3
                if j == 0 or j == 1 or j == 2:
                    quadj = quad1
                elif j == 3 or j == 4 or j == 5:
                    quadj = quad2
                else:
                    quadj = quad3
                
                for i in quadi:
                    for j in quadj:
                        if grid[i][j] == val:
                            quadCount += 1
                if quadCount > 1:
                    return False
    return True