# Length of the longest substring
class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        char_index = {}
        # Initialize the starting point of the current window and the maximum length
        start = 0
        max_len = 0
        
        # Loop through the string
        for end in range(len(S)):
            # If we find a repeating character within the current window, move the start point
            if S[end] in char_index and char_index[S[end]] >= start:
                start = char_index[S[end]] + 1
            
            # Update the last seen index of the current character
            char_index[S[end]] = end
            
            # Update the maximum length
            max_len = max(max_len, end - start + 1)
        
        return max_len