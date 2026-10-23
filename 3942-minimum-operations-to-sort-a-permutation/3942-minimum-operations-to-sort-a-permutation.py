class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pos = nums.index(0)

        ans = float('inf')

        # Case 1: Rotate the original array
        if all(nums[(i + pos) % n] == i for i in range(n)):
            ans = min(ans, pos, n - pos + 2)

        # Case 2: Reverse the array, then rotate
        rev = nums[::-1]
        k = rev.index(0)

        if all(rev[(i + k) % n] == i for i in range(n)):
            ans = min(ans, min(k, n - k) + 1)

        return ans if ans != float('inf') else -1
        