class Solution:
    def partitionLabels(self, S):

        # sort to diction
        result = {}
        for i in range(len(S)):
            if not S[i] in result.keys():
                result[S[i]] = [i, i]
            else:
                result[S[i]][1] = i

        curinterval = [0, 0]
        cursize = []
        for i in result:
            if result.get(i)[0] <= curinterval[1] < result.get(i)[1]:
                curinterval[1] = result.get(i)[1]
            elif result.get(i)[0] > curinterval[1]:
                cursize.append(curinterval[1]-curinterval[0]+1)
                curinterval = [result.get(i)[0], result.get(i)[1]]
        cursize.append(curinterval[1]-curinterval[0]+1)
        return cursize

#
# # test case
# test = Solution()
# S = "ababcbacadefegdehijhklij"
# print(test.partitionLabels(S))
