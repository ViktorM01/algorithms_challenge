def lower(x: int, a: []) -> int:
    l, r = 0, n - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans

def upper(x: int, a: []) -> int:
    l, r = 0, n - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if a[mid] <= x:
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    return ans


n = int(input())
a = list(map(int, input().split()))
k = int(input())
a.sort()

for i in range(k):
    l, r = map(int, input().split())
    L = lower(l, a)
    R = upper(r, a)
    if a[L] >= l and a[R] <= r:
        print(R - L + 1, end = ' ')
    else:
        print(0, end = ' ')
