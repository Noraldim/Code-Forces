for _ in range(int(input())):
    ln = int(input())
    mx = list(map(int , input().split()))
    even  = [n for n in mx if n%2 == 0]
    odd  = [n for n in mx if n%2 == 1]
    new_od = sorted(odd , reverse=True)
    if len(odd)%2 == 1:
        x = int((len(odd)/2)+1)
    else:
        x = int(len(odd)/2)
    if len(odd) == 0 :
        print(0)
        continue
    new_odd = new_od[0:x:1]
    print(sum(even) + sum(new_odd))
