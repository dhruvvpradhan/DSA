class Solution(object):

    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for i in range(n):
            product = 1
            g = 0
            l = 1

            for j in range(i, n):
                product *= nums[j]

                # Calculate GCD
                a, b = g, nums[j]
                while b:
                    a, b = b, a % b
                g = a

                # Calculate LCM
                l = (l * nums[j]) // self.gcd(l, nums[j])

                if product == g * l:
                    ans = max(ans, j - i + 1)

        return ans

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a