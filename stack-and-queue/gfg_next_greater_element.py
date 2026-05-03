from typing import List


class Solution:

    def next_greater_element(self, arr) -> List[int]:
        stack = []
        ans = [-1] * len(arr)
        size = len(arr)
        for i in range(size - 1, -1, -1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(arr[i])
        return ans

    def brute_force(self, arr) -> List[int]:
        ans = [-1] * len(arr)
        size = len(arr)
        for i in range(size):
            for j in range(i + 1, size):
                if arr[i] < arr[j]:
                    ans[i] = arr[j]
                    break
        return ans


nums = [1, 3, 2, 4]
s = Solution()
print(s.brute_force(nums))
print(s.next_greater_element(nums))
