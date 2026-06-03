###Leetcode Link : https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=array

class TwoSum:
    def CheckPairs(nums,target):
        recorded = {}
        for i,num in enumerate(nums):
            if(target - num) in recorded:
                return [recorded[target - num],i]
            recorded[num] = i


##Used Hashmap as the complexity is O(1) and for linear searfh it will be O(n)
##So overall the complexity becomes(O(n*1)) = O(n)


if __name__ == "__main__":
    nums =[2,7,7,9,0]
    target=9
    print(TwoSum.CheckPairs(nums,target))

