import math
import sys

# Using sys.stdin.readline can be faster for large inputs
# input = sys.stdin.readline

def gcd(a, b):
    """Calculates the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a) # Ensure result is non-negative

def gcd_list(lis):
    """Calculates the greatest common divisor of a list of numbers."""
    if not lis:
        # This should ideally not happen if n >= 2
        # If it could, decide on behavior (e.g., return 0 or raise error)
        # For this problem, C will have at least one element if n >= 2.
         return 0 # Or handle as error
    if len(lis) == 1:
        return abs(lis[0]) # Ensure non-negative

    res = abs(lis[0])
    for i in range(1, len(lis)):
        res = gcd(res, abs(lis[i]))
        # Optimization: if gcd becomes 1, it will stay 1
        if res == 1:
            return 1
    return res

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # 1. Check if all elements are the same
    all_same = True
    for i in range(1, n):
        if a[i] != a[0]:
            all_same = False
            break

    if all_same:
        print("No")
        return

    # 2. If not all same, a solution exists. Print Yes.
    print("Yes")

    # 3. Try partition B = {a[0]}, C = {a[1], ..., a[n-1]}
    # Note: a[1:] handles n=2 correctly (gives [a[1]])
    # gcd_list handles single-element list correctly
    gcd_c_partition1 = gcd_list(a[1:])
    gcd_b_partition1 = abs(a[0]) # GCD of single element is itself (abs value)

    if gcd_b_partition1 != gcd_c_partition1:
        # This partition works
        ans = [2] * n
        ans[0] = 1
        print(*ans)
    else:
        # 4. First partition failed (gcds were equal). Find another.
        # We know another exists. Find the first element different from a[0].
        diff_idx = -1
        for j in range(1, n):
            if a[j] != a[0]:
                diff_idx = j
                break
        
        # Create the partition B = {a[diff_idx]}, C = {rest}
        # This partition is guaranteed to work in this case.
        ans = [2] * n
        ans[diff_idx] = 1
        print(*ans)


t = int(input())
for _ in range(t):
    solve()
