##https://leetcode.com/problems/single-number/submissions/1970804526/


def Find_single(nums):
    result = 0
    for num in nums:
        result ^= num

    return result     

