n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))
 
 
for x in q:
    l, r = 0, n - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    if a[n - 1] < x:
        print(n + 1)
    else:
        print(ans + 1)
