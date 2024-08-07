n, s = map(int, input().split())
a = list(map(int, input().split()))
 
# i, j = 0, 0
# ans = []
max_n, sum_seg = 0, 0
j = 0
 
for i in range(n):
    while j < n and sum_seg + a[j] <= s:
        sum_seg += a[j]
        j += 1
    max_n = max(max_n, j - i)
    sum_seg -= a[i]
 
 
print(max_n)
