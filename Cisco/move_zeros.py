##https://leetcode.com/problems/move-zeroes/description/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_zero_pos = 0
        for i in range(0,len(nums)):
            if(nums[i] != 0):
                nums[current_zero_pos],nums[i] = nums[i],nums[current_zero_pos]
                current_zero_pos += 1  


        