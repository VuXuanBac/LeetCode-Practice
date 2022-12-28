# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

def count_subarray(nums: list[int], k: int) -> int:
    def bsearch(nums: list[int], start : int, end : int, threshold) -> int:
        low, high = start, end
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] * (mid - start + 1) >= threshold:
                high = mid
            else:
                low = mid + 1

        return high - (nums[high] * (high - start + 1) >= threshold)

    first = last = len(nums) - 1
    sum = [0] * len(nums)
    count = 0
    for i in range(len(nums)):
        for j in range(first, last + 1):
            sum[j] += nums[first]
        last = bsearch(sum, first, last, k)
        first -= 1
        count += last - first

    return count

count_subarray([2,1,4,3,5], 10)
#count_subarray([4,3,8,4,2,9,5,8,1,3], 100)

def check(func, inputs: list[str], outputs: list[str], input_converter = None, output_converter = None, deserialize = False):
    length = min(len(inputs), len(outputs))
    for i in range(length):
        ip = input_converter(inputs[i]) if input_converter else inputs[i]
        eop = output_converter(outputs[i]) if output_converter else outputs[i]
        op = func(*ip) if deserialize else func(ip)
        print(f'Test {i}: {eop == op} : {op} : {eop}')

with open('input.txt', 'r') as fin, open('output.txt', 'r') as fout:
    inputs = fin.readlines()
    outputs = fout.readlines()

def str2strlist(s: str) -> list[str]:
    if s[0] == '[' and s[-1] == ']':
        return s[1:-1].split(',')

    return []

def input_converter(s: str) -> tuple[list[str], int]:
    s1, s2 = s.split(' ', 2)
    return str2strlist(s1), int(s2)
# check(count_subarray, inputs, outputs, input_converter, int)
