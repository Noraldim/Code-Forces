t = int(input())

for _ in range(t):
    ln , k = map(int , input().split())
    mx = list(map(int, input().split()))
    mxmaxfr = max(mx)
    mxmin = min(mx)
    mxsum = sum(mx)
    mxmaxnumber = mx.index(mxmaxfr)
    mx[mxmaxnumber] -= 1
    mxmaxsc = max(mx)
    if (mxmaxsc - mxmin) > k:
        print("Jerry")
        continue
    if mxsum % 2 == 1:
        print("Tom")
        continue
    else:
        print("Jerry")
        continue
