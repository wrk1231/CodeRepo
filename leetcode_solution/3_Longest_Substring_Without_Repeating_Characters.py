class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s);
        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            record = [1]*length;
           
            i = 0
            j = 0
            while(i <= length ):
                while(i<= length -1  and s[i] not in s[j:i]):
                    i += 1;
                record[j] = i - j
                if(i == length):
                    break;
                else:
                    j = i-1

                    # greedy
                    while(s[i] != s[j]):
                        j -= 1
                    j += 1

            return max(record)
