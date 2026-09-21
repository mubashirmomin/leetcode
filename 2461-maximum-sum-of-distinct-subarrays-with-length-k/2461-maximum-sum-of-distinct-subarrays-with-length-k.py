class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        left = 0
        count = {}
        window_sum = 0 
        max_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            count[nums[right]] = count.get(nums[right],0) +1

            if right - left + 1 > k:
                window_sum -= nums[left]
                count[nums[left]] -= 1

                if count[nums[left]] == 0:
                    del count[nums[left]]

                left += 1

            if right - left + 1 == k and len(count) == k:
                max_sum = max(max_sum,window_sum)

        return max_sum