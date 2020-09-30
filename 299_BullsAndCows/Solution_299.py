class Solution:
    def getHint(self, secret, guess):
        dictSecret = {}
        dictGuess = {}
        A = 0
        B = 0
        for i in range(len(secret)):
            if secret[i] in dictSecret.keys():
                dictSecret[secret[i]].append(i)
            else:
                dictSecret[secret[i]] = [i]

        for i in range(len(guess)):
            if guess[i] in dictSecret.keys():
                if i in dictSecret[guess[i]]:
                    A += 1
                    dictSecret[guess[i]].remove(i)
                else:
                    if guess[i] in dictGuess.keys():
                        dictGuess[guess[i]].append(i)
                    else:
                        dictGuess[guess[i]] = [i]

        for i in dictGuess.keys():
            B += min(len(dictGuess[i]), len(dictSecret[i]))
        return str(A) + 'A' + str(B) + 'B'


# # test case
# test = Solution()
# secret = "1123"
# guess = "0111"
# print(test.getHint(secret, guess))
