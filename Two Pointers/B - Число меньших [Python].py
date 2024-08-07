n, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
lst = []
l = 0
 
for r in range(len(b)):
    while l < len(a) and a[l] < b[r]:
        l += 1
    print(l, end = ' ')
