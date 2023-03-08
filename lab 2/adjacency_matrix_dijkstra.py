import sys
import random
import time

def dijkstra_adj_matrix(G, s):
    n = len(G)
    dist = [sys.maxsize] * n
    dist[s] = 0
    visited = [False] * n
    pq = [s]

    while pq:
        u = pq.pop(0)
        visited[u] = True
        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                if dist[u] + G[u][v] < dist[v]:
                    dist[v] = dist[u] + G[u][v]
                    if v not in pq:
                        pq.append(v)

    return dist


def random_adj_matrix(n, density):
    G = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u != v and random.random() < density:
                G[u][v] = random.randint(1, 10)
    return G

def time_dijkstra_adj_matrix(n, density):
    G = random_adj_matrix(n, density)
    s = random.randint(0, n-1)
    start_time = time.time()
    dist = dijkstra_adj_matrix(G, s)
    end_time = time.time()
    print(f"n={n}, density={density}, time={end_time-start_time:.6f}s")

for n in [10, 50, 100, 200, 1000, 2000]:
    for density in [0.1, 0.3, 0.5, 0.7, 0.9]:
        time_dijkstra_adj_matrix(n, density)