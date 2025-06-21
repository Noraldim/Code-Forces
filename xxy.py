def sp_mx(m):
    matrix = [[0] * m for _ in range(m)]
    x = y = m // 2 
    dx_dy = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction = 0
    steps = 1
    num = 0
    matrix[x][y] = num
    num += 1

    while steps < m:
        for _ in range(2):  # Two directions for the same step size
            dx, dy = dx_dy[direction]
            for _ in range(steps):
                x += dx
                y += dy
                matrix[x][y] = num
                num += 1
            direction = (direction + 1) % 4
        steps += 1

    # Final top row
    for _ in range(m - 1):
        x += dx_dy[direction][0]
        y += dx_dy[direction][1]
        matrix[x][y] = num
        num += 1

    return matrix
x = 5
result = sp_mx(x)

print(result)
