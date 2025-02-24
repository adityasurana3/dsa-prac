class Solution:
    def segregate0and1(self, arr):
        left = 0
        right = len(arr) - 1
        while(left < right):
            # print('left',left)
            # print('right',right)
            while(arr[left] == 0 and left < right):
                left += 1
            while(arr[right] == 1 and left < right):
                right -= 1
            if(left < right):
                temp = arr[right]
                arr[right] = arr[left]
                arr[left] = temp
                left += 1
                right -= 1
        
            
            
s = Solution()
s.segregate0and1([0, 0, 0, 1, 0])