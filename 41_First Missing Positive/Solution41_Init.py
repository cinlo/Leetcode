class Solution:
    def firstMissingPositive(self, nums):
        # the max of the missing one is the length + 1
        n = len(nums) + 1
        nums = list(set(nums))
        for i in range(1, n):
            if i not in nums:
                return i
        return n

# test = Solution()
# nums = [3,4,-1,1]
# print(test.firstMissingPositive(nums))