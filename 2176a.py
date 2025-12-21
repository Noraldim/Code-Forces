t = int(input())
for _ in range(t):
    count = 0
    ln = int(input())
    li = list(map(int, input().split()))
    iflag = True
    i = 0 
    ix = 1
    for x in range(len(li)):     
        if ix+1 > len(li):
            break
        elif li[i] > li[ix]:
            count+=1
            ix += 1
        elif li[i] <= li[ix]:
            i = ix 
            ix +=1
    print(count)
    continue

