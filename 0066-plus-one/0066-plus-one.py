class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lis=[]
        sum = ""
        for num in digits:
            sum += str(num)
        inti = int(sum) + 1
        sum = str(inti)
        for ch in sum:
            lis.append(int(ch))
        return lis

