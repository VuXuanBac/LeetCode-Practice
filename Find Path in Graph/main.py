# https://leetcode.com/problems/find-if-path-exists-in-graph/
def exist_path_BFS(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    adjacent_edges = [set() for _ in range(n)]

    for [v1, v2] in edges:
        adjacent_edges[v1].add(v2)
        adjacent_edges[v2].add(v1)

    visited = [False] * n
    Q = [source]

    while len(Q) > 0:
        
        u = Q.pop(0)
        if u == destination:
            return True

        if not visited[u]:
            visited[u] = True
            for v in adjacent_edges[u]:
                Q.append(v)
    
    return False

def exist_path_DFS(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    adjacent_edges = [set() for _ in range(n)]

    for [v1, v2] in edges:
        adjacent_edges[v1].add(v2)
        adjacent_edges[v2].add(v1)

    visited = [False] * n
    Q = [source]

    while len(Q) > 0:
        
        u = Q.pop()
        if u == destination:
            return True

        if not visited[u]:
            visited[u] = True
            for v in adjacent_edges[u]:
                if not visited[v]:
                    Q.append(v)
    
    return False

def check(func, inputs: list[str], outputs: list[str], input_converter = None, output_converter = None, deserialize = False):
    length = min(len(inputs), len(outputs))
    for i in range(length):
        ip = input_converter(inputs[i]) if input_converter else inputs[i]
        eop = output_converter(outputs[i]) if output_converter else outputs[i]
        op = func(*ip) if deserialize else func(ip)
        print(f'Test {i}: {eop == op} : {op} : {eop}')

with open('input.txt', 'r') as fin, open('output.txt', 'r') as fout:
    inputs = fin.readlines()
    outputs = fout.readlines()

def str2intlistlist(s: str) -> list[list[int]]:
    result = []
    if s[0] == '[' and s[-1] == ']':
        sub_list_str = s[1:-1].replace('],[', ']#[').split('#')
        for sl in sub_list_str:
            result.append([int(c) for c in sl[1:-1].split(',')])

    return result

def input_converter(s: str) -> tuple[int, list[list[int]], int, int]:
    ip = s.split(' ')
    return (int(ip[0]), str2intlistlist(ip[1]), int(ip[2]), int(ip[3]))

check(exist_path_DFS, inputs, outputs, input_converter, int, deserialize = True)
