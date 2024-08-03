n, k = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = int(input())
 
def bin_search(mid, a, k):
    sum = 0
    for i in range(len(a)):
        sum += int(a[i] / mid)
    return sum >= k
 
l, r = 0, 10**12
ans = 0
 
for i in range(100):
    mid = (l + r) / 2
    if bin_search(mid, a, k):
        l = mid
        ans = mid
    else:
        r = mid
print(ans)
