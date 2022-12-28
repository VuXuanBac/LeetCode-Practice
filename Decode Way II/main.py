# https://leetcode.com/problems/decode-ways-ii/
def count_decoding(s: str) -> int:
    mod = 10**9 + 7
    # count[0]: total
    # count[1]: end with 1
    # count[2]: end with 2
    count = [1, 0, 0]
    for c in s:
        if c == '*':
            count = [(9 * count[0] + 9 * count[1] + 6 * count[2]) % mod, 
                        count[0],
                        count[0]]
        else:
            count = [((c > '0') * count[0] + count[1] + (c <= '6') * count[2]) % mod,
                     (c == '1') * count[0],
                     (c == '2') * count[0]]

    return count[0]

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

check(count2, inputs, outputs, None, int)
