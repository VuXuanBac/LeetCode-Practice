# https://leetcode.com/problems/longest-valid-parentheses/
# Idea: DP
# vpl[i]: The longest valid parentheses end at i-1 in the input string

def longest_valid(s: str) -> int:
    vpl = [0] * (len(s) + 1)
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                vpl[i + 1] = 2 + vpl[i - 1]
                continue

            t = vpl[i]    # t <= i
            if t == 0 or t == i:
                vpl[i + 1] = 0
                continue

            if s[i - t - 1] == '(':
                vpl[i + 1] = t + 2 + vpl[i - t - 1]
    return max(vpl)
        

    
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

check(longest_valid, inputs, outputs, None, int)
