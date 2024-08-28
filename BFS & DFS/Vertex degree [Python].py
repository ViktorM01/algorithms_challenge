N = 100
n = 0
edges = [[] for _ in range(N)]
graph = [[0] * N for _ in range(N)]
lst = []

def read():
    global n
    n = int(input())
    for _ in range(n):
        lst.append(sum(list(map(int, input().split()))))

def solver():
    print(*lst)

if __name__ == "__main__":
    read()
    solver()
