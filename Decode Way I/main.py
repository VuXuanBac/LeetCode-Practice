# https://leetcode.com/problems/decode-ways-i/
def count_decoding(s: str) -> int:
    count = (1, 0)
    for i in range(len(s)):
        if s[i] == '0':
            if i == 0 or s[i-1] not in ['1', '2']:
                return 0
            count = (0, count[0])

        else:
            if i > 0 and '11' <= s[i-1:i+1] <= '26':
                count = (count[0] + count[1], count[0])
            else:
                count = (count[0] + count[1], 0)
    
    return count[0] + count[1]

            

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

check(count_decoding, inputs, outputs, None, int)
