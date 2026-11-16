class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            result = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]

                total = 0
                for digit in group:
                    total += int(digit)

                result += str(total)

            s = result

        return s