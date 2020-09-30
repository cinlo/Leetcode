class Solution:
    def firstMissingPositive(self, nums):
        # the max of the missing one is the length + 1
        nums.append(0)
        n = len(nums)

        # add 0 so it won't be selected
        print(nums)
        for i in range(n):
            if nums[i] >= n or nums[i] < 0:
                nums[i] = 0
        for i in range(n):
            nums[nums[i] % n] += n
        for i in range(n):
            if nums[i] // n == 0:
                return i
        return n

# test = Solution()
# nums = [3,4,-1,1]
# print(test.firstMissingPositive(nums))