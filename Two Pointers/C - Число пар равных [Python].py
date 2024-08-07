n, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
i, j = 0, 0
ans = []
 
for j in range(l):
    counter = 0
    while i < n and a[i] <= b[j]:
        if a[i] == b[j]:
            counter += 1
        i += 1
    if j > 0 and b[j] == b[j-1]:
        ans.append(ans[-1])
    else:
        ans.append(counter)
 
print(sum(ans))
