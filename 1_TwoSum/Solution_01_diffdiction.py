class Solution:
    def twoSum(self, nums, target):
        resultdic = {}
        for i in range(len(nums)):
            if nums[i] in resultdic:
                return [resultdic[nums[i]], i]
            else:
                resultdic[target - nums[i]] = i
# # test
# test = Solution()
# nums = [3, 3]
# target = 6
# print(test.twoSum(nums, target))
