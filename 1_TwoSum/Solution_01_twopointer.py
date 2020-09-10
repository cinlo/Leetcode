class Solution:
    def twoSum(self, nums, target):
        resultdic = {}
        for i in range(len(nums)):
            if nums[i] in resultdic:
                resultdic[nums[i]].append(i)
            else:
                resultdic[nums[i]] = [i]
        nums.sort()

        min = 0
        max = len(nums) - 1
        while min < max:
            if nums[min] + nums[max] > target:
                max -= 1
            if nums[min] + nums[max] < target:
                min += 1
            if nums[min] + nums[max] == target:
                if nums[min] != nums[max]:
                    return [resultdic.get(nums[min])[0], resultdic.get(nums[max])[0]]
                else:
                    return resultdic.get(nums[min])

# # test
# test = Solution()
# nums = [3, 3]
# target = 6
# print(test.twoSum(nums, target))
