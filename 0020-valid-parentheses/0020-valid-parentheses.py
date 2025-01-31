class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        # Dictionary to match closing brackets with opening ones
        mapping = {")": "(", "}": "{", "]": "["}
        # Iterate through each character in the string
        for char in s:
            if char in mapping:  # If it's a closing bracket
                # Pop the top of the stack, if stack is empty return a mismatch
                top_element = stack.pop() if stack else '#'
                # If the top element of the stack does not match the expected opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it to the stack
                stack.append(char)
        # If the stack is empty, all brackets matched correctly, else there's an unmatched opening bracket
        return not stack


