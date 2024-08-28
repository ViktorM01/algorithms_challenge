N = 100
n = 0
edges = [[] for _ in range(N)]
graph = [[0] * N for _ in range(N)]
lst = []

def read():
    global n
    n = int(input())
    for i in range(n):
        graph[i] = list(map(int, input().split()))


def solver():
    ans = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                ans += 1
                edges[i].append(j)

    print(n, ans)
    for i in range(n):
        for x in edges[i]:
            print(i + 1, x + 1)


if __name__ == "__main__":
    read()
    solver()
