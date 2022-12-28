# I: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# II: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

def profit_1(prices: list[int]) -> int:
    # DP: profit[i] = profit if sell on day i
    m, profit = prices[0], 0
    for p in prices:
        profit = max(profit, p - m)
        m = min(m, p)
    
    return profit

def profit_2(prices: list[int]) -> int:
    # DP: profit = sum(buy on lowest price before rising and sell at highest price before decaying)
    profit = 0
    for i in range(1, len(prices)):
        profit += max(0, prices[i] - prices[i - 1])
    
    return profit

# def check(func, inputs: list[str], outputs: list[str], input_converter = None, output_converter = None):
#     length = min(len(inputs), len(outputs))
#     for i in range(length):
#         ip = input_converter(inputs[i]) if input_converter else inputs[i]
#         op = output_converter(outputs[i]) if output_converter else outputs[i]
#         result = func(ip) == op
#         print(f'Test {i}: {result}')

# with open('input.txt', 'r') as fin, open('output.txt', 'r') as fout:
#     inputs = fin.readlines()
#     outputs = fout.readlines()

# def str2intlist(s: str) -> list[int]:
#     last_index = -1
#     if s[-1] == '\n':
#         last_index = -2
#     if s[0] == '[' and s[last_index] == ']':
#         return [int(c) for c in s[1:last_index].split(',')]
#     return []

# check(profit, inputs, outputs, str2intlist, int)
