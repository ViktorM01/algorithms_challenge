def func(x, y, k):
    left, right = 0, max(x, y) * 2 // k + 2
 
    while left < right:
        step = (left + right) // 2
        x_step = (step + 1) // 2 
        y_step = step // 2 
 
        if x_step * k >= x and y_step * k >= y:
            right = step
        else:
            left = step + 1 
 
    return left
 
t = int(input())
results = []
 
for _ in range(t):
    x, y, k = map(int, input().split())
    results.append(func(x, y, k))
 
for result in results:
    print(result)
