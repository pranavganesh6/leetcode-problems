class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # Start at the initial altitude of 0
        altitude = 0
        max_altitude = 0

        # Calculate cumulative altitude at each point
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)

        return max_altitude

# Example usage
solution = Solution()
print(solution.largestAltitude([-5, 1, 5, 0, -7]))  # Output: 1
print(solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # Output: 0x
