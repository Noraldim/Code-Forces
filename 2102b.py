t = int(input())

for _ in range(t):
    ln = int(input())
    mx = list(map(int, input().split())) 
    f = mx[0]
    yy = abs(f) 
    mmx = sorted(mx)
    xx = int(ln/2)
    work = mx[:]
    work.pop(0)
    num = 0 
    worksort = sorted(work)
    if f == min(mx):
        print("NO")
        continue
    if mmx[xx] == f:
        print("YES")
        continue
    for x in worksort:
        num = num+1
        if x == yy:
            break
    if num <= ln and num >= ln/2:
        print("YES")
        continue
    else:
        print("YES")
        continue
   
