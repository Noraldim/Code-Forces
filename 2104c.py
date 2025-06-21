t = int(input())

for _ in range(t):
    ln = int(input())
    mx = list(map(str ,input().strip()))
    if ln == 2:
        if mx[0] == 'B':
            print("Bob")
            continue
        else:
            print("Alice")
            continue
    temp = []
    tempa = []
    for x in mx:
        if x == 'B':
            temp.append(x)
        else: 
            tempa.append(x)   
    if ln == 3:
        if len(temp) == 2:
            print("Bob")
            continue
        else:
            print("Alice")
            continue
    if mx[0] == mx[-1]:
        if mx[0] == 'B':
            print("Bob")
            continue
        else:
            print("Alice")
            continue  
    if ln == 4 :
        if len(tempa) == 3 :
            print("Alice")
            continue 
        if len(temp) == 3:
            print("Bob")
            continue
    if mx[-1] == mx [-2]:
        if mx[-1] == 'B':
            print("Bob")
            continue
        if mx[-1] == 'A':
            print("Alice")
            continue
    if len(temp) == len(tempa):
        print("Bob")
        continue
    if mx[-1] == 'B':
        if len(temp) > 2:
            print("Bob")
            continue
    if len(temp) > len(tempa):
        print("Bob")
        continue
    if len(temp) == ln -1 :
        print("Bob")
        continue
    if len(tempa) == ln - 1:
        print("Alice")
        continue
    print("Bob")
    continue
