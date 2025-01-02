# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of numbers
        num_indices = {}

        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_indices:
                # Return the indices of the complement and current number
                return [num_indices[complement], i]

            # Add the current number and its index to the dictionary
            num_indices[num] = i  # Fix here: use `i` as the value, not `1`

# Example usages:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
