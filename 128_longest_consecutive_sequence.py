from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        max_len = 0
        for i in nums:
            nums_set.add(i)
        for i in nums_set:
            if(i-1) in nums_set:
                continue
            else:
                count = 1
                while(i+count) in nums_set:
                    count += 1
                max_len = max(max_len, count)
        return max_len
    

s = Solution()
result = s.longestConsecutive([100,4,200,1,3,2])
print(result)
        
