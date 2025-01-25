class Solution:
    def increasingTriplet(self, nums) -> bool:
        """
        Given an integer array nums, return true if there exists a triple of indices (i, j, k)
        such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exist, return false.

        Parameters
        ----------
        nums : List[int]
            The input array of integers.

        Returns
        -------
        bool
            True if there exists a triplet (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k], otherwise False.
        """
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # update first if num is smaller than or equal to first
            elif num <= second:
                second = num  # update second if num is smaller than or equal to second
            else:
                # if we find a number greater than both first and second, we have our triplet
                return True
        
        return False

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    nums3 = [2, 1, 5, 0, 4, 6]
    print(solution.increasingTriplet(nums1))  # Output: True
    print(solution.increasingTriplet(nums2))  # Output: False
    print(solution.increasingTriplet(nums3))  # Output: True