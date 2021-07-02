def rotateImage(a):
    # invert matrix along diagonal
    n = len(a)
    i = 0
    for row in a:
        j = 0
        for col in row:
            if i == j:
                continue
            else:
                a[i][j], a[j][i] = a[j][i], a[i][j]
            j += 1
        i += 1
        
    # flip matrix along middle vertical
    # works for both even and odd sized matrices because n // 2 leaves out odd middle column
    i = 0
    for row in a:
        col = 0
        while col < n // 2:
            a[i][col], a[i][n - col - 1] = a[i][n - col - 1], a[i][col]
            col += 1
        i += 1

    return a
    