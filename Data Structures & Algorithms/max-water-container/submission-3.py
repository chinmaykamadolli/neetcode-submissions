class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        res = 0
        while l < r:
            area = (r - l) * min(h[l], h[r])
            res = max(area, res)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return res
        