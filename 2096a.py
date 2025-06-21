t = int(input())

for _ in range(t):
    ln = int(input())
    mx = list(map(str, input().strip()))
    small = []
    larg = []
    result = []
    for x in mx :
        if x == '>':
            larg.append(x)
        else:
            small.append(x)
    larg_ln = len(larg)
    small_ln = len(small)
    result.append(small_ln+1)
    xx = small_ln + 1 
    yy = small_ln + 1 
    for y in mx:
        if y == '<':
            yy = yy - 1
            result.append(yy)
        else:
            xx = xx + 1
            result.append(xx)
    print(*result)
