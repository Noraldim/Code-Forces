t = int(input())

def solve(mx):
    res = 0
    bun = 2
    bn = 1
    for i in range(len(mx)-1):
        if len(set(mx)) == 1:
            res = 0
        elif mx[0] == 0 and mx[-1] == 0:
            res+=bun
            if mx[i] == 0 and mx[i+1] ==0 :
                res += 1
            bun = 0
        elif mx[i] == 0 and mx[i+1] == 0:
            res+=1
            res+=bn
            bn =0
        else:
            res+= bn
            bn = 0
            
           

    return res

for _ in range(t):
    ln = int(input())
    mx = input().strip()
    mx = [int(x) for x in mx]
    one = [x for x in mx if x == 1]
    zero = [ x for x in mx if x == 0]
    lnone = len(one)
    lnzero = len(zero)

    result = solve(mx)
    print(result)

   

