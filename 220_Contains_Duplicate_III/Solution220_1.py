class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # check null
        if k < 0 or t < 0 or len(nums) < 0:
            return False

        # Bucket O(N)
        LevelResult = {}
        for i in range(len(nums)):
            cur_level = nums[i] // (t + 1)
            if nums[i] < 0:
                cur_level = cur_level - 1

            # find solution in same level
            if cur_level not in LevelResult:
                LevelResult[cur_level] = i
            else:
                if i - LevelResult.get(cur_level) > k:
                    LevelResult[cur_level] = i
                else:
                    return True
            # find solution in other level
            pre_level = cur_level - 1
            next_level = cur_level + 1
            if LevelResult.get(pre_level) is not None:
                if i - LevelResult.get(pre_level) <= k and abs(nums[LevelResult.get(pre_level)] - nums[i]) <= t:
                    return True
            if LevelResult.get(next_level) is not None:
                if i - LevelResult.get(next_level) <= k and abs(nums[LevelResult.get(next_level)] - nums[i]) <= t:
                    return True
        return False


        # # Brute Force - O(N^2) & O(1)
        # if t == 0 and len(nums) == len(set(nums)):
        #     return False
        # for i in range(len(nums)):
        #     for j in range(i + 1, i + k + 1):
        #         if j >= len(nums):
        #             break
        #         if abs(nums[i] - nums[j]) <= t:
        #             return True
        # return False




# Test Case
test = Solution()
nums = [3,18,5]
k = 4
t = 4
print(test.containsNearbyAlmostDuplicate(nums, k, t))
