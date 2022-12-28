# I: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

def profit_3(prices: list[int]) -> int:
    # based on profit_1
    # profit[1..N] = max(profit[1..X] + profit[X+1...N]) -> O(n^2)
    # -> Inno 1: Calculate 2 times: left-to-right and right-to-left -> O(2n)
    min_left, profit_left = prices[0], [0] * len(prices)
    for i in range(1, len(prices)):
        profit_left[i] = max(profit_left[i-1], prices[i] - min_left)
        min_left = min(prices[i], min_left)
    

    max_right, profit_right, max_profit = prices[-1], 0, 0
    for i in range(len(prices) - 2, -1, -1):
        profit_right = max(profit_right, max_right - prices[i])
        max_profit = max(max_profit, profit_right + profit_left[i])
        max_right = max(prices[i], max_right)

    return max_profit

def check(func, inputs: list[str], outputs: list[str], input_converter = None, output_converter = None):
    length = min(len(inputs), len(outputs))
    for i in range(length):
        ip = input_converter(inputs[i]) if input_converter else inputs[i]
        eop = output_converter(outputs[i]) if output_converter else outputs[i]
        op = func(ip)
        print(f'Test {i}: {eop == op} : {op}')

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

check(profit_3, inputs, outputs, str2intlist, int)
