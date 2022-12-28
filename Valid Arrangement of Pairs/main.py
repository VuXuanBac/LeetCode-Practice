# https://leetcode.com/problems/find-if-path-exists-in-graph/

def valid_arrangement(pairs: list[list[int]]) -> list[list[int]]:
    info = []
    adj = []
    vertext_index = {}
    # build vertext info list
    for (start, end) in pairs:
        if start not in vertext_index:
            sind = len(adj)
            info.append([start, 1])
            adj.append([])
            vertext_index[start] = sind
        else:
            sind = vertext_index[start]
            info[sind][1] += 1


        if end not in vertext_index:
            eind = len(info)
            info.append([end, -1])
            adj.append([])
            vertext_index[end] = eind
        else:
            eind = vertext_index[end]
            info[eind][1] -= 1

        adj[sind].append(eind)
    start = 0
    for i in range(len(info)):
        if info[i][1] > 0:
            start = i
            break

    # Hierholzer’s Algorithm
    st = [start]
    euler = []
    while st:
        u = st[-1]
        if adj[u]:
            v = adj[u].pop()
            st.append(v)
        else:
            euler.append(st.pop())

    # Build result list
    result = []
    for i in range(len(euler) - 1, 0, -1):
        start = info[euler[i]][0]
        end = info[euler[i-1]][0]
        result.append([start, end])

    return result

valid_arrangement([[12,18],[2,8],[400,2],[18,6],[18,7],[6,2],[400,12],[2,18],[8,400]])

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

# check(valid_arrangement, inputs, outputs, str2intlistlist, str2intlistlist)
