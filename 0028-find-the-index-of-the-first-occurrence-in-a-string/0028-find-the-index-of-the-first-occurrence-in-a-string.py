class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If the needle is an empty string, return 0
        if not needle:
            return 0
        # Iterate over the haystack to find the first occurrence of needle
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i  # Return the index of the first occurrence
        # If no occurrence is found, return -1
        return -1
