# https://leetcode.com/problems/maximum-product-subarray/

def max_product_subarray(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    p = (0, 0)
    # p[0]: positive product of subarray end at i
    # p[1]: negative product of subarray end at i
    # if x = nums[i] > 0: p = ( max(p[0] * x, x), p[1] * x )
    # else p = ( p[1] * x, min(p[0] * x, x) )
    result = -100
    for n in nums:
        x = (p[0] + (p[0] == 0)) * n
        y = p[1] * n
        p = (x, y) if n > 0 else (y, x)
        result = max(result, p[0])
    
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

check(max_product_subarray, inputs, outputs, str2intlist, int)
