import copy


class Solution:
    def largestTimeFromDigits(self, A) -> str:
        A.sort()
        if A[0] > 2:
            return ""
        if A[0] < 2 and A[1] >= 6:
            return ""
        if A[0] == 2 and (A[1] > 3 or A[2] >= 6):
            return ""
        result = [-1, -1, -1, -1]

        # if the first is 2
        checklist = copy.deepcopy(A)
        for i in range(3, -1, -1):
            if checklist[i] == 2:
                result[0] = 2
                checklist.pop(i)
                break

        for i in range(2, -1, -1):
            if checklist[i] < 4:
                result[1] = checklist[i]
                checklist.pop(i)
                break

        for i in range(1, -1, -1):
            if checklist[i] < 6:
                result[2] = checklist[i]
                checklist.pop(i)
                break

        if len(checklist) == 1:
            result[3] = checklist[0]
            result.insert(2, ':')
            res = ''.join([str(elem) for elem in result])
            return res

        # if the first is 1 or 0
        result = [-1, -1, -1, -1]
        checklist = copy.deepcopy(A)
        for i in range(3, -1, -1):
            if checklist[i] == 1:
                result[0] = 1
                checklist.pop(i)
                break
        if len(checklist) == 4:
            result[0] = 0
            checklist.pop(0)

        result[1] = checklist[2]

        if checklist[1] < 6:
            result[2] = checklist[1]
            result[3] = checklist[0]
        else:
            result[2] = checklist[0]
            result[3] = checklist[1]
        result.insert(2, ':')
        res = ''.join([str(elem) for elem in result])
        return res


# # Test Case
# test = Solution()
# A = [0, 3, 1, 0]
# print(test.largestTimeFromDigits(A))
