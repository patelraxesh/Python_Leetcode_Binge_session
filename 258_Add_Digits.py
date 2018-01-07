'''
258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

## Unoptimized soltion
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numb = str(num)
        total = 0
        
        if len(numb) == 1:
            return int(numb)
        
        while(len(str(numb)) > 1):
            total = 0
            for i in numb:
                total += int(i)
            numb = str(total)
        
        return total
        
## Optimal solution
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
          return 0
        else:
          return 1 + ( (num-1) % 9 )


