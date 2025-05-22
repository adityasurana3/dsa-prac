from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # d1 = {}
        # l1 = []
        # sorted_str = list(map(lambda x: ''.join(sorted(x)), strs))
        # for i in sorted_str:
        #     if i not in d1:
        #         d1[i] = []
        
        # for i in strs:
        #     sorted_i = ''.join(sorted(i))
        #     if sorted_i in d1.keys():
        #         list_str = d1.get(sorted_i)
        #         list_str.append(i)
        #         d1[sorted_i] = list_str
                
        # for i in d1.values():
        #     l1.append(i)
        # return l1
        
        ############## Frequency array ###################
        '''
        result = {}
        for word in strs:
            freq_arr = [0] * 26
            for i in word:
                freq_arr[ord(i) - ord('a')] += 1
            key = tuple(freq_arr)
            if key not in result:
                result[key] = [word]
            else:
                result[key].append(word)
        
        return list(result.values())
        '''

s = Solution()
result = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

print(result)