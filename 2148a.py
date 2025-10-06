t = int(input())

for _ in range(t):
    n , m , x ,y = map(int , input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [z for z in a if z != x]
    b = [e for e in b if b != y]

    print(len(a)+len(b))
