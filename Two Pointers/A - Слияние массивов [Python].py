n, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
lst = []
l, r = 0, 0
while l <= len(a) - 1 and r <= len(b) - 1:
    if a[l] <= b[r]:
        lst.append(a[l])
        l += 1
    elif a[l] > b[r]:
        lst.append(b[r])
        r += 1
 
if l == (len(a)):
    lst.extend(b[r:])
if r == (len(b)):
    lst.extend(a[l:])
 
print(*lst)
