class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        separate = need1 * cost1 + need2 * cost2

        # Option 2: Buy type 3 for all requirements
        both = max(need1, need2) * costBoth

        # Option 3: Buy type 3 for overlapping requirements
        # and purchase the remaining items separately
        overlap = min(need1, need2) * costBoth
        remaining = abs(need1 - need2)

        if need1 > need2:
            overlap += remaining * cost1
        else:
            overlap += remaining * cost2

        return min(separate, both, overlap)
        