for _ in range(int(input())):
    n, k = map(int, input().split())

    if n == 2:
        if k == 4:
            print("UU")
            print("UU")
        elif k in (1, 3):
            print("NO")
        elif k == 2:
            print("UU")
            print("LR")
        continue

    matrix = [['D' for _ in range(n)] for _ in range(n)]
    target = 0

    if (n*n) - k >= 4:
        for x in range(n):
            if target < k:
                matrix[0][x-1] = "U"
                target+=1
        for x in range(n):
            if target < k :
                matrix[0][x-1] = "R"
                target+=1
        for x in range(n):
            for y  in range(n):
                if target < k and target[x][y] == 'D':
                    matrix[x][y] == "U"
        for x in range(n):
            if x == 0:
                matrix[n-1][x] == "U"
            if x == 1 :
                matrix[n-1][x] == "L"
        for x in range(n):
            if x == 0:
                matrix[n-2][x] == "R"
            if x == 1:
                matrix[n-2][x] == "D"
        for x in range(n):
            if matrix[n-1][x] != "R" and matrix[n-1][x] != "L" and matrix[n-1][x] != "D" and matrix[n-1][x] != "U":
                matrix[n-1][x] == "L"

        for x in range(n):
            if matrix[n-1][x] != "R" and matrix[n-1][x] != "L" and matrix[n-1][x] != "D" and matrix[n-1][x] != "U":
                matrix[x][n-1] == "L"
       


    print("YES")
    for row in matrix:
        print(''.join(row))

