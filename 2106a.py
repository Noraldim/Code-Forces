t = int(input())

for _ in range(t):
    xx = int(input())   
    xm = list(map(int, input().strip()))
    c0  = 0
    c1 = 0
    one = 0
    two = 0
    for x in xm:
        if x == 1:
            c1 +=1
        elif x == 0:
            c0 +=1
    one = (c1 - 1)*c1 if c1 >=1 else 0
    two = (c1 + 1)*c0
    print(one+two) 
