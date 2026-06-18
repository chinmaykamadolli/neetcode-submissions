class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = {}
        maxf = 0
        res = 0
        l = 0
        for r in range(len(s)):
            max_len[s[r]] = 1 + max_len.get(s[r], 0)
            maxf = max(maxf, max_len[s[r]])

            while (r - l +1) - maxf > k:
                max_len[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res