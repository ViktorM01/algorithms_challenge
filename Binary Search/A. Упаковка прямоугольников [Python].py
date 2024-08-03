w, h, n = map(int, input().split())
 
l, r = 0, 10**18
ans = 0
while l <= r:
    mid = (l + r) // 2
    if (mid // w) * (mid // h) >= n:
        r = mid - 1
        ans = mid
    else:
        l = mid + 1
 
print(ans)
