class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define the Roman numeral mappings
        roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        # Initialize the result string
        result = ""
        
        # Convert the number to Roman numerals
        for value, symbol in roman_numerals:
            while num >= value:
                result += symbol  # Append the symbol to the result
                num -= value      # Subtract the value from the number
                
        return result

# Example usage
solution = Solution()
print(solution.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(solution.intToRoman(58))    # Output: "LVIII"
print(solution.intToRoman(1994))  # Output: "MCMXCIV"
