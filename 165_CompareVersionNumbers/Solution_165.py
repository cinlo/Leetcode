class Solution:
    def compareVersion(self, version1, version2):
        cur_v1sum = 0
        v1list = []
        for i in range(len(version1)):
            if version1[i] != ".":
                cur_v1sum += cur_v1sum * 10 + int(version1[i])
                continue
            else:
                v1list.append(cur_v1sum)
                cur_v1sum = 0
        v1list.append(cur_v1sum)

        cur_v2sum = 0
        v2list = []
        for i in range(len(version2)):
            if version2[i] != ".":
                cur_v2sum += cur_v2sum * 10 + int(version2[i])
                continue
            else:
                v2list.append(cur_v2sum)
                cur_v2sum = 0
        v2list.append(cur_v2sum)

        vlistlen = max(len(v1list), len(v2list))

        for i in range(vlistlen):
            if len(v1list) < i + 1:
                v1list.append(0)
            if len(v2list) < i + 1:
                v2list.append(0)
            if v1list[i] > v2list[i]:
                return 1
            if v1list[i] < v2list[i]:
                return -1
        return 0
#
# # test case
# test = Solution()
# print(test.compareVersion("1.0.1", "1"))
