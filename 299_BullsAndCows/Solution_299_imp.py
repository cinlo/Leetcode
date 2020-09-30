from collections import Counter
class Solution:
    def getHint(self, secret, guess):
        A = sum([x == y for x, y in zip(secret, guess)])
        count_sec = Counter(secret)
        count_quess = Counter(guess)
        B = sum(min(count_sec[elem], count_quess[elem]) for elem in count_sec) - A
        return str(A) + 'A' + str(B) + 'B'

# # test case
# test = Solution()
# secret = "1123"
# guess = "0111"
# print(test.getHint(secret, guess))
