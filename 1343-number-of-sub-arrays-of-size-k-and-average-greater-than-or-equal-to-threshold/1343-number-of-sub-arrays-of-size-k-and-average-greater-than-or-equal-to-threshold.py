class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        count = 0

        target = threshold * k 

        if window_sum >= target:
            count += 1 

        for right in range(k,len(arr)):
            window_sum += arr[right]
            window_sum -= arr[right - k]

            if window_sum >= target:
                count += 1

        return count 