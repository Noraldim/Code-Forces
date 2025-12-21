t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()   
    mx = [int(x) for x in s]
    res = 0
    trak =0
    if len(set(mx)) == 1 and mx[0] == 0:
        res = len(mx)
        print(res)
        continue
    for index , x in enumerate(mx):
        if trak + 1 <= len(mx):
            if mx[trak] == 1:
                trak += k
            elif mx[trak] == 0:
                res += 1
            trak+=1
    print(res)     
