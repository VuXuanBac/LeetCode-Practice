# https://leetcode.com/problems/find-if-path-exists-in-graph/

def TopoSortingDFS(numCourses: int, prerequisites: list[list[int]]) -> list:
    status = [0] * numCourses # 0: not visited, 1: not done (in stack), 2: done

    edges = [[] for _ in range(numCourses)]
    for p in prerequisites:
        edges[p[0]].append(p[1])
    
    topo = []

    for root in range(numCourses):
        if status[root] > 0:
            continue
        stack = [root]
        while stack:
            u = stack[-1]
            if status[u] > 0:
                if status[u] == 1:
                    topo.append(u)
                    status[u] = 2
                stack.pop()
                continue

            # elif status[u] = 0:
            status[u] = 1
            for v in edges[u]:
                if status[v] == 0:
                    stack.append(v)
                elif status[v] == 1:
                     return []

    return topo


def TopoSorting(numCourses: int, prerequisites: list[list[int]]) -> bool:
    source = []
    indeg = [0] * numCourses
    edges = [[] for _ in range(numCourses)]
    topo = []

    for p in prerequisites:
        edges[p[1]].append(p[0])
        indeg[p[0]] += 1
    for i in range(numCourses):
        if indeg[i] == 0:
            source.append(i)

    while source:
        u = source.pop()
        topo.append(u)
        for v in edges[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                source.append(v)
    if len(topo) < numCourses:
        return []
    return topo

    

def check(func, inputs: list[str], outputs: list[str], input_converter = None, output_converter = None, deserialize = False):
    length = min(len(inputs), len(outputs))
    for i in range(length):
        ip = input_converter(inputs[i]) if input_converter else inputs[i]
        eop = output_converter(outputs[i]) if output_converter else outputs[i]
        op = func(*ip) if deserialize else func(ip)
        r = 'Correct' if eop == op else 'Incorrect'
        m = f'--- {op}/Expected {eop}' if eop != op else ''
        print(f'Test {i + 1}: {r} {m}')

with open('input.txt', 'r') as fin, open('output.txt', 'r') as fout:
    inputs = fin.readlines()
    outputs = fout.readlines()

def str2intlistlist(s: str) -> list[list[int]]:
    result = []
    if s[-1] == '\n':
        s = s[:-1]
    if s[0] == '[' and s[-1] == ']':
        sub_list_str = s[1:-1].replace('],[', ']#[').split('#')
        for sl in sub_list_str:
            result.append([int(c) for c in sl[1:-1].split(',')])

    return result

def input_converter(s: str) -> tuple[int, list[list[int]]]:
    ip = s.split(' ')
    return (int(ip[0]), str2intlistlist(ip[1]))

check(TopoSorting, inputs, outputs, input_converter, int, deserialize = True)
