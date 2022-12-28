# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

def minimum_path(grid: list[list[int]], moveCost: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    INF = 999999999
    p = [v for v in grid[0]]
    for r in range(1, rows):
        temp = []
        for c in range(cols):
            mp = INF
            for i in range(cols):
                mp = min(mp, p[i] + moveCost[grid[r - 1][i]][c])
            temp.append(grid[r][c] + mp)
        p = temp
    
    return min(p)


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
def input_converter(s: str):
    x = s.split(' ', 2)
    return str2intlistlist(x[0]), str2intlistlist(x[1])

check(minimum_path, inputs, outputs, input_converter, int, deserialize=True)
