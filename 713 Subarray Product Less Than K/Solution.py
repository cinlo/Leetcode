class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        n = len(nums)
        p, i, j, total = 1, 0, 0, 0
        while j < n:
            p = p * nums[j]
            while i <= j and p >= k:
                p = p / nums[i]
                i += 1
            total += (j - i + 1)
            j += 1
        return total


test = Solution()
nums = [10, 5, 2, 6]
k = 100
print(test.numSubarrayProductLessThanK(nums, k))
