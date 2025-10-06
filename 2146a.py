def numCount(bo, index):
    res = 0 
    for x in bo:
        if x >= index:
            res+=1
    return res

t = int(input())
for _ in range(t):
    ln = int(input())
    mx = list(map(int , input().split()))
    new_mx = []
    final_list = []
    if len(mx) == len(set(mx)):
        print(len(mx))
        continue
    for x in set(mx) :
        count = 0
        for y in mx :
            if y == x:
                count+=1
        new_mx.append(count)
    for x in new_mx:
        result = numCount(new_mx,x)
        fin = x * result
        final_list.append(fin)
    print(max(final_list))
