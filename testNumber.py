class Solution(object):

    def __init__(self):
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        self.resultlist = []

    def combine(self, combinations, digits):

        temp = self.phone
        for i in digits:
            if i not in temp:
                print("error")
                # exit(0)
                self.input()
        if not digits:
            self.resultlist.append(combinations)
        else:
            for char in self.phone[digits[0]]:
                self.combine(combinations + char, digits[1:])
        return self.resultlist

    @staticmethod
    def input():
        rawDigits = input("Input:")
        listDigits = list(rawDigits)
        value = []

        if '[' in listDigits  or ']' in listDigits:
            listDigits.remove("[")
            listDigits.remove("]")

        for i in listDigits:
            if ',' == i or '0' == i or '1' == i:
                continue
            value.append(i)

        # print(value)
        return value



value = Solution.input()
print("Output:", Solution().combine('', value))


