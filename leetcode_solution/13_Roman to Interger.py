class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # turn string into list
        romanToInteger = {'I': 1, "V": 5, "X": 10,
                          "L": 50, "C": 100, "D": 500, "M": 1000}


        prev = 1000000
        result = 0
        for i in range(len(s)):
            result += romanToInteger[s[i]]
            if prev < romanToInteger[s[i]]:
                result -= 2 * prev
            prev = romanToInteger[s[i]]
        return result
