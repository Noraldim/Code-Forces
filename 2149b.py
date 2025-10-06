t = int(input())

for _ in range(t):
    ln = int(input())
    mx = list(map(int, input().split()))
    st_mx = sorted(mx)
    new_list = [st_mx[i+1] - st_mx[i] for i in range(0 , len(mx)-1,2)]
    print(max(new_list))
