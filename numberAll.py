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
      self.resultList = []

  def combine(self, combinations, digits):

      temp = self.phone
      for i in digits:
          if i not in temp:
              print("error")
              self.input()
      if not digits:
          self.resultList.append(combinations)
      else:
          for char in self.phone[digits[0]]:
              self.combine(combinations + char, digits[1:])
      return self.resultList

  @staticmethod
  def input():
      for digits in range(100):
          value = ""
          # print (digits)
          digits = str(digits)
          print ("Input:%s" % digits)

          for i in digits:
              if '0' == i or '1' == i:
                  continue
              value += i
          if value == '':
              print("Output:null")
          else:
              print("Output:", Solution().combine('', value))

Solution.input()