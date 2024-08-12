n, s = map(int, input().split())
a = list(map(int, input().split()))
 
l, sum_, ans = 0, 0, 0
 
for r in range(n):
    sum_ += a[r]
    while sum_ > s:
        sum_ -= a[l]
        l += 1
    len_ = r - l + 1
    ans += len_ * (len_ + 1) // 2
 
print(ans)
