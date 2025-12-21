t = int(input())

def solve(li):
    l = li[0]
    a = li[1]
    b = li[2]
    result = []

    for i in range(l+1):
        y = a + i*b
        yy = y%l
        result.append(yy)
    return(max(result))

for _ in range(t):
    mx = list(map(int, input().split()))
    result = 0 
    result= solve(mx)
    print(result)
    
