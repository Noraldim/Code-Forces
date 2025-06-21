def gcd(a,b):
    while b:
        a , b = b , a%b
    return a 
def gcd_list(lis):
    res = lis[0]
    for x in lis[1:]:
        res = gcd(res,x)
    return res
t = int(input())
for _ in range(t):
    
    ln = int(input())
    mx = list(map(int, input().split()))
    f = False
    for x in range(1,ln):
        left = mx[:x]
        right = mx[x:]
        one = gcd_list(left)
        two = gcd_list(right)
        if one != two:
            print("YES") 
            xx = list(1 for x in range(len(left)))
            yy = list(2 for x in range(len(right)))
            print(*(xx+yy))
            f = True
            break
    if not f:
        print("NO")

