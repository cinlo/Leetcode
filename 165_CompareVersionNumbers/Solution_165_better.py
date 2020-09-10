class Solution:
    def compareVersion(self, version1, version2):
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]

        vlistlen = max(len(v1), len(v2))

        for i in range(vlistlen):
            if len(v1) < i + 1: v1.append(0)
            if len(v2) < i + 1: v2.append(0)
            if v1[i] > v2[i]: return 1
            if v1[i] < v2[i]: return -1
        return 0
#
# # test case
# test = Solution()
# print(test.compareVersion("1.0.1", "1"))
