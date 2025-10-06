t = int(input())
for _ in range(t):
    ln  = int(input())
    mx  = list(map(int, input().split()))
    
    dis = set(mx)
    dis_len = len(dis)
 
    print(dis_len + (dis_len-1))

