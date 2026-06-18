class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        window = [0] * 26
        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1
        
        if need == window:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            leftChar = ord(s2[l]) - ord('a')
            window[leftChar] -= 1

            rightChar = ord(s2[r]) - ord('a')
            window[rightChar] += 1

            if need == window:
                return True

            l += 1
        return False