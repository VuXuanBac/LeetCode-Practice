# https://leetcode.com/problems/valid-parentheses/
def is_valid(s: str) -> bool:
    open_close_mapping = {')': '(', ']': '[', '}': '{'}
    open_stack = []
    for c in s:
        if c in '({[':
            open_stack.append(c)
        elif c in ')]}':
            if len(open_stack) == 0:
                return False

            if open_close_mapping[c] == open_stack[-1]:
                open_stack.pop()
            else:
                return False

    return len(open_stack) == 0

def check(func, inputs: list[str], outputs: list[str], input_converter = None, output_converter = None):
    length = min(len(inputs), len(outputs))
    for i in range(length):
        ip = input_converter(inputs[i]) if input_converter != None else inputs[i]
        op = output_converter(outputs[i]) if output_converter != None else outputs[i]
        result = func(ip) == op
        print(f'Test {i}: {result}')

with open('input.txt', 'r') as fin, open('output.txt', 'r') as fout:
    inputs = fin.readlines()
    outputs = fout.readlines()

def str2intlist(s: str) -> list[int]:
    if s[0] == '[' and s[-1] == ']':
        return [int(c) for c in s[1:-1].split(',')]

check(is_valid, inputs, outputs, None, bool)
