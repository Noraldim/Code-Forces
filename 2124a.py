t = int(input())
for _ in range(t):
    ln = int(input())
    mx = list(map(int , input().split()))
    sort_mx = sorted(mx)
    flag = True
    while(flag == True):
        for index, x in enumerate(mx):
            if mx[index] == sort_mx[index]:
            print("NO")
            flag = False
            break
    if flage == True:
        for x in range(len(mx)):
            mx.pop()
            new_mx_sorted = sorted(mx)
            for index , x in enumerate(mx):
                if mx[index] == new_mx_sorted[index]:
                    print("YES")
                    print(len(mx))
                    print(*mx)
                    break


