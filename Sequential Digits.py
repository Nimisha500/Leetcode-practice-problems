# https://leetcode.com/problems/sequential-digits
class Solution:
    def sequentialDigits(self, low: int, high: int):
        ans=[]
        for i in range(1,10):
            num=i
            for j in range(i+1,10):
                num=num*10+j
                if(num>=low and num<=high):
                    ans.append(num)
        ans.sort()
        return ans









low = 1000
high = 13000
print(Solution().sequentialDigits(low,high))