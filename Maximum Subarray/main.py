# https://leetcode.com/problems/maximum-subarray/

def max_subarray(nums: list[int]) -> int:
    result = nums[0]
    max_at_i = 0
    for n in nums:
        max_at_i = max(n, max_at_i + n)
        result = max(result, max_at_i)
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

def str2intlist(s: str) -> list[int]:
    last_index = -1
    if s[-1] == '\n':
        last_index = -2
    if s[0] == '[' and s[last_index] == ']':
        return [int(c) for c in s[1:last_index].split(',')]
    return []

check(max_subarray, inputs, outputs, str2intlist, int)
