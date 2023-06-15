nums = [-1, -2, -3, -4, -5]
target = -8
class Solution(object):
    def twoSum(nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
    print(twoSum(nums, target))