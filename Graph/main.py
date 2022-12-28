def exist_path_BFS(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    adjacent_edges = [set() for _ in range(n)]

    for [v1, v2] in edges:
        adjacent_edges[v1].add(v2)
        adjacent_edges[v2].add(v1)

    visited = [False] * n
    Q = [source]

    while Q:
        
        u = Q.pop(0)
        if u == destination:
            return True

        if not visited[u]:
            visited[u] = True
            for v in adjacent_edges[u]:
                Q.append(v)
    
    return False


def DFS(N: int, edges: list[list[int]], source: int):
    time = 0
    visited = [-1] * N
    done = [-1] * N
    stack = [source]
    father = [-1] * N
    while stack:
        u = stack.pop()
        print('Pop', u)
        if visited[u] == -1:
            visited[u] = time
            time += 1
            for v in edges[u].__reversed__():
                if visited[v] == -1:
                    print('Push', v)
                    stack.append(v)
                    father[v] = u
            
            done[u] = time
            time += 1

    print('====== DFS FROM', source, '======')
    print('Visited:', visited)
    print('Done   :', done)
    print('Father :', father)


DFS(9, [[1],[2,3],[5,6],[2,4],[1],[3,7,8],[0],[8],[]], 0)
# DFS(9, [[1],[2,3],[5,6],[2,4],[1],[3,7,8],[0],[8],[]], 1)
# DFS(9, [[1],[2,3],[5,6],[2,4],[1],[3,7,8],[0],[8],[]], 4)