class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0 

        for num in arr1:
            is_far = True

            for x in arr2:
                if abs(num - x) <= d:
                    is_far = False
                    break
            if is_far:
                count +=1
        return count

        