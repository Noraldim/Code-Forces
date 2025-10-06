for _ in range(int(input())):
    ln = int(input())
    mx = list(map(int , input().split()))
    index = 2
    for x in range(1 , len(mx)-1):
        if mx[x-1] > mx[x] and mx[x+1] > mx[x] :
            print("NO")
            index = 4
    while(index == 2):
        print("YES")
        break
