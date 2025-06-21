t = int(input())

for _ in range(t):
  
    mx = list(map(int, input().split()))
    sumx = sum(mx)
    if sumx %3 != 0:
        print("NO")
        continue
    if mx[-2] > sumx/3:
        print("NO")
        continue 
    print("YES")
