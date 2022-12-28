# https://leetcode.com/problems/number-of-matching-subsequences/

def count_subsequence(s: str, words: list[str]) -> int:
    trie = {'_': 0}
    result = len(words)
    for key in words:
        cur_node = trie
        for c in key:
            if c not in cur_node:
                parent_value = cur_node.get('_', 0)
                current_value = s.find(c, parent_value)
                cur_node[c] = {'_': current_value + 1 if current_value > -1 else -1}
                if current_value == -1: # not found
                    result -= 1
                    break
            elif cur_node[c].get('_', 0) == -1:
                result -= 1
                break

            cur_node = cur_node[c]

    return result


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

def str2strlist(s: str) -> list[str]:
    if s[0] == '[' and s[-1] == ']':
        return s[1:-1].split(',')

    return []

def input_converter(s: str) -> tuple[str, list[str]]:
    s1, s2 = s.split(' ', 2)
    if s2[-1] == '\n':
        return s1, str2strlist(s2[:-1])
    return s1, str2strlist(s2)

check(count_subsequence, inputs, outputs, input_converter, int, deserialize = True)
