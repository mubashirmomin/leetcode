class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        target = {}
        window = {}
        result = []

        for char in p:
            target[char] = target.get(char,0)+1

        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1

            if right - left + 1 > len(p):
                window[s[left]] -= 1

                if window[s[left]] ==0:
                    del window[s[left]]

                left += 1 

            if window == target:
                result.append(left)

        return result