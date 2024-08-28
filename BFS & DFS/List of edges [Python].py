N = 100
n = 0
edges = [[] for _ in range(N)]
graph = [[0] * N for _ in range(N)]
lst = []

def read():
    global m, n
    m, n = map(int, input().split())
    for _ in range(n):
        l = list(map(int, input().split()))
        lst.append(l)
        
def solver():
    global fin_lst
    fin_lst = [[0] for i in range(m)]
    for ind in lst:
        fin_lst[ind[0]-1][0] += 1
        fin_lst[ind[0]-1].append(ind[1])

    print(m)
    for i in fin_lst:
        j = i
        if len(i) > 1:
            j = [i[0]] + sorted(i[1:])
        print(*j)

if __name__ == "__main__":
    read()
    solver()
