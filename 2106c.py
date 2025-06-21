t = int(input())

for _ in range(t):
    siz , mx = map(int,input().split()) 
    a = list(map(int, input().split())) 
    b = list(map(int, input().split()))
    if all(x == -1 for x in a) or all(y == -1 for y in b):
        big = max(a)
        small = min(a)
        xx = small + mx 
        yy = xx - big 
        print(yy+1)
        continue
    res = []
    nres = []
    for x,y in zip(a,b):
        if y==-1 :
            nres.append(x)
            continue
        res.append(x+y)
    mnres = max(nres) if nres else -1
    
    if all(x == res[0] for x in res):
       if mnres <= res[0]:
           if (min(a) + mx) < res[0]:
               print(0)
               continue
           else:
               print(1)
               continue
       else: 
           print(0)
    else:
        print(0)
        continue

    
