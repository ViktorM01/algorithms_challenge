t = int(input())
lst = []
 
for _ in range(t):
    n = int(input())
    maps = [input().strip() for _ in range(n)]
    lst.append(maps)
 
f_lst = []
for map_ in lst:
    cols = []
    for row in reversed(map_):
        for col in range(4):
            if row[col] == '#':
                cols.append(col + 1)
                break
    f_lst.append(cols)
 
for x in f_lst:
    print(*x)
