class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(current, open_count, close_count):
            # Base case: when the current string has reached the maximum length
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an open parenthesis if possible
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Add a close parenthesis if it would form a valid combination
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        # Initialize the result list
        result = []
        backtrack("", 0, 0)  # Start with an empty string
        return result

# Example usage:
solution = Solution()
print(solution.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
print(solution.generateParenthesis(1))  # Output: ["()"]
