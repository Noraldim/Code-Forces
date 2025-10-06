t = int(intput())

for _ in range(t):
    data = list(map(int , input().split()))
    n = data[0]
    playerOne = data[1:3]
    playerTwo = data[3:5]

    if n <= 2 :
        print(1)
        continue

