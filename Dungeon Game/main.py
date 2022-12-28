# https://leetcode.com/problems/dungeon-game/

def minimum_hp(dungeon: list[list[int]]) -> int:
    m = len(dungeon)
    n = len(dungeon[0])
    INF = 9999999
    down = [INF for _ in range(n)]
    right = 1
    down[n - 1] = 1
    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            x = down[c] - dungeon[r][c]
            y = right - dungeon[r][c]
            down[c] = right = min((x - 1)*(x > 0), (y - 1)*(y > 0)) + 1
        
        right = INF
    return down[0]



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

check(minimum_hp, inputs, outputs, str2intlistlist, int)
