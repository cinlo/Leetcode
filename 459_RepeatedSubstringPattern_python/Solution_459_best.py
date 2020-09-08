class Solution:
    def repeatedSubstringPattern(self, s):
        length = len(s)
        result = {}
        for i in range(len(s)):
            if s[i] in result:
                result[s[i]] = result[s[i]] + 1
            else:
                result[s[i]] = 1

        for i in range(len(result)):

        print (result)

        #
        # for i in range(1, length//2 + 1):
        #     if length % i == 0 and s[:i] * (length // i) == s:
        #         return True
        # return False

# test case
test = Solution()
s = "abcabcabcabc"
print(test.repeatedSubstringPattern(s))
