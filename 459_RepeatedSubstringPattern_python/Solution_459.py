class Solution:
    def repeatedSubstringPattern(self, s):
        # check null
        if len(s) <= 1:
            return False

        # start
        presubstring = ''
        cursubstring = ''
        j = 0
        for i in range(len(s)):

            # print("this is i ", i, s[i])
            # print("this is presubstring", presubstring)
            # print("this is postsubstring", s[(len(s)-len(presubstring)):len(s)])
            # print("this is cursbustring", cursubstring)

            cursubstring += str(s[i])

            if presubstring != s[(len(s)-len(presubstring)):len(s)]:
                presubstring += cursubstring
                cursubstring = ''
                # print('case 1')
                continue

            if presubstring == '' or s[i] != presubstring[j]:
                presubstring += str(cursubstring)
                cursubstring = ''
                j = 0
                # print('case 2')
                continue

            j = (j + 1) % len(presubstring)

        if len(cursubstring) % len(presubstring) == 0 and len(s) != len(presubstring):
            return True

        return False


# # # test case
# test = Solution()
# s = "ababab"
# print(test.repeatedSubstringPattern(s))
