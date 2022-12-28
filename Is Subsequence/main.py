# https://leetcode.com/problems/is-subsequence/
def is_subsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True

    same_count = 0
    for c in t:
        if c == s[same_count]:
            same_count += 1
            if same_count == len(s):
                return True

    return False

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

def extract_str(s: str) -> tuple[str]:
    s1, s2 = s.split(' ', 2)
    if s2[-1] == '\n':
        return s1, s2[:-1]
    return s1, s2

check(is_subsequence, inputs, outputs, extract_str, int, deserialize = True)
