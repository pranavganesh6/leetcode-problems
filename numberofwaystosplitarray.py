class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize variables
        total_sum = sum(nums)  # Total sum of the array
        left_sum = 0  # Sum of the first part
        valid_splits = 0  # Count of valid splits

        # Iterate through the array
        for i in range(len(nums) - 1):  # Stop at n - 1 because there must be at least one element on the right
            left_sum += nums[i]  # Add current element to left sum
            right_sum = total_sum - left_sum  # Calculate the right sum
            
            # Check the condition for a valid split
            if left_sum >= right_sum:
                valid_splits += 1

        return valid_splits

# Examples: 
solution = Solution()
print(solution.waysToSplitArray([10, 4, -8, 7]))  # Output: 2
print(solution.waysToSplitArray([2, 3, 1, 0]))    # Output: 2
