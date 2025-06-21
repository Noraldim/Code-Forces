t = int(input())
def swap(matrix, row1, col1, row2, col2):
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

def sp_mx(n):
    matrix = [[0]*n for _ in range(n)]
    x = y = n // 2
    if n % 2 == 0:
        x -= 1
        y -= 1
    matrix[y][x] = 0
    value = 1
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    step = 1
    while value < n * n:
        for d in range(4):
            dx, dy = directions[d]
            for _ in range(step):
                x += dx
                y += dy
                if 0 <= x < n and 0 <= y < n:
                    matrix[y][x] = value
                    value += 1
                    if value >= n * n:
                        break
            if d == 1 or d == 3:
                step += 1
    return matrix
    for row in matrix:
        print(" ".join(f"{x:2}" for x in row))
 
for x in range(t):
    mx = int(input())
    xx = [[0,1],[2,3]]
    yy = [[8,4,5],[6,0,1],[7,2,3]]
    if mx == 2:
        for x in xx:
            print(" ".join(map(str, x)))
        continue
    if mx == 3:
        for x in yy:
            print(" ".join(map(str, x)))
        continue
    n = mx 
    result = sp_mx(n)
    for x in result :
        print(" ".join(map(str, x)))

