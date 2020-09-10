class Solution:
    def reorderLogFiles(self, logs):
        digitloglist = []
        letterloglist = []
        for i in range(len(logs)):
            secondword = logs[i].split()[1][0]
            if secondword.isalpha():
                print(secondword)
                digitloglist.append(logs[i])
            else:
                letterloglist.append(logs[i])

        def neworder(log):
            allpartlogs = log.split()
            key, rest = allpartlogs[0], allpartlogs[1:]
            orderresult = ' '.join(rest) + ' ' + key
            return orderresult

        digitloglist.sort(key=neworder)
        result = digitloglist + letterloglist
        return result

# # test case
# test = Solution()
# logs = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
# print(test.reorderLogFiles(logs))
