class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        window_count = 0

        for i in range(k):
            if s[i] in vowels:
                window_count +=1

        max_count = window_count 

        left = 0

        for right in range(k,len(s)):

            if s[left] in vowels:
                window_count -=1

            left +=1

            if s[right] in vowels:
                window_count +=1

            max_count = max (window_count,max_count)

        return max_count