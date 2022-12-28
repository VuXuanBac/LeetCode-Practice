# https://leetcode.com/problems/generate-parentheses/
def generate(n: int) -> list[str]:
    result = []
    def Try(remain: int, sum: int, cur: str) -> None:
        if remain == 0:
            if sum == 0:
                result.append(cur)
            return
        if sum == 0:
            Try(remain - 1, 1, cur + '(')
        else:
            for i in [-1, 1]:
                Try(remain - 1, sum + i, cur + ('(' if i > 0 else ')'))
    
    Try(n, 0, '')
    print(result)
    return result

for i in range(1, 9):
    generate(i)


# def check(func, inputs: list[str], outputs: list[str], input_converter = None, output_converter = None, deserialize = False):
#     length = min(len(inputs), len(outputs))
#     for i in range(length):
#         ip = input_converter(inputs[i]) if input_converter else inputs[i]
#         eop = output_converter(outputs[i]) if output_converter else outputs[i]
#         op = func(*ip) if deserialize else func(ip)
#         r = 'Correct' if eop == op else 'Incorrect'
#         m = f'--- {op}/Expected {eop}' if eop != op else ''
#         print(f'Test {i + 1}: {r} {m}')

# with open('input.txt', 'r') as fin, open('output.txt', 'r') as fout:
#     inputs = fin.readlines()
#     outputs = fout.readlines()

# def str2strlist(s: str) -> list[str]:
#     if s[0] == '[' and s[-1] == ']':
#         return s[1:-1].split(',')

# check(generate, inputs, outputs, int, str2strlist)
