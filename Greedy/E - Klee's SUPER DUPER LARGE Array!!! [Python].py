import math
 
 
def find_min_x(n, k):
    a = 1
    b = 2 * k - 1
    c = -n * (2 * k + n - 1) // 2
 
    D = b * b - 4 * a * c
 
    i1 = (-b + math.sqrt(D)) / (2 * a)
    i2 = (-b - math.sqrt(D)) / (2 * a)
 
    i = int(i1 if i1 > 0 else i2)
 
    min_x = float('inf')
    for idx in [i - 1, i, i + 1]:
        if idx >= 1 and idx <= n:
            left_sum = idx * (2 * k + idx - 1) // 2
            total_sum = (2 * k + n - 1) * n // 2
            x = abs(2 * left_sum - total_sum)
            min_x = min(min_x, x)
 
    return min_x
 
t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    results.append(find_min_x(n, k))
 
for result in results:
    print(result)
