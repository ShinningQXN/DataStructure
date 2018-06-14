next permutation
找规律
12345
12354
12435
12453
12534
12543
13245
13254

25431
35421
31245

class Solution:
    def nextPermutation(self, s):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(s)
        j = n - 2
        while j >= 0 and s[j] >= s[j + 1]: j -= 1
        i = n - 1 
        if j >= 0:
            while i >= 0 and s[i] <= s[j]:
              i -= 1
            s[i], s[j] = s[j], s[i]
        s[j + 1:] = s[j + 1:][::-1]

  
  
 25431
 j = 0
 i = 3
 35421
 31254
 
 11431-13114
 13411
 11431
 12134
123
