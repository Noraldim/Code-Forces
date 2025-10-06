t = int(input())

for _ in range(t):
    x , y = map(int , input().split())
    if y%2 == 1:
        print(x)
    else:
        print(0)

