class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c= a+b
        return bin(int(a,2) +int(b,2))[2:]