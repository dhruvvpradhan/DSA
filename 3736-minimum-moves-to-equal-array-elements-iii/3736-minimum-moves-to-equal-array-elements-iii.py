class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = max(nums)
        moves = 0
        for num in nums:
            moves += target - num    

        return moves
        