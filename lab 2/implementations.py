import sys

#Implementation using Adjacency Matrix and Array-based Priority Queue:
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


#Implementation using Adjacency List and Heap-based Priority Queue:
import sys
import heapq

def dijkstra_adj_list(G, s):
    n = len(G)
    dist = [sys.maxsize] * n
    dist[s] = 0
    visited = [False] * n
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

    return dist
