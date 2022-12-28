# https://leetcode.com/problems/find-if-path-exists-in-graph/

def check_courses_stack(numCourses: int, prerequisites: list[list[int]]) -> bool:
    status = [0] * numCourses # 0: not visited, 1: not done (in stack), 2: done
    edges = [[] for _ in range(numCourses)]
    for p in prerequisites:
        edges[p[0]].append(p[1])
    
    for root in range(numCourses):
        if status[root] > 0:
            continue
        stack = [root]
        while stack:
            u = stack[-1]
            if status[u] > 0:
                status[u] = 2
                stack.pop()
                continue

            # elif status[u] = 0:
            status[u] = 1
            for v in edges[u]:
                if status[v] == 0:
                    stack.append(v)
                elif status[v] == 1:
                    return False

    return True


def check_courses(numCourses: int, prerequisites: list[list[int]]) -> bool:
    pre = [0] * numCourses
    post = [0] * numCourses
    time = 0
    edges = [[] for _ in range(numCourses)]
    for p in prerequisites:
        edges[p[0]].append(p[1])

    def DFS(root: int) -> bool:
        nonlocal pre, post, time
        time += 1
        pre[root] = time
        for v in edges[root]:
            if pre[v] == 0: # not visited
                if not DFS(v):
                    return False
            elif post[v] == 0: # visited but not done (current in stack)
                return False
        time += 1
        post[root] = time
        return True
            
    for v in range(numCourses):
        if pre[v] == 0:
            if not DFS(v):
                return False

    return True

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

check(check_courses_stack, inputs, outputs, input_converter, int, deserialize = True)
