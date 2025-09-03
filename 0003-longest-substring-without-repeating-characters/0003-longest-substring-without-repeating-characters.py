class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start = 0
        max_len = 0

        #abcabcbb

        for i, n in enumerate(s):
            if n in char_index and char_index[n] >= start:
                start = char_index[n] + 1
            char_index[n] = i
            max_len = max(max_len, i - start + 1)
        return max_len