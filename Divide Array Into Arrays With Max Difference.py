# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference

class Solution:
    def divideArray(self, nums, k):
        nums=sorted(nums)
        print(nums)
        if len(nums)%3 !=0:
            return []
        ans=[]
        st=[nums[0]]
        i=1
        while(i<len(nums)):
            print(len(st), nums[i]-nums[i-1])
            if(len(st)<3 and nums[i]-nums[i-1]<=k):
                st.append(nums[i])
                print(st)
                if(len(st)==3 and st[2]-st[0]<=k):
                    ans.append(st)
                    if((i+1)!=len(nums)):
                        st=[nums[i+1]]
                        i=i+1

            else:
                return []
            i=i+1
        
        if(len(ans) == len(nums)//3):
            return ans
        return []




nums = [15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2]
k = 2
print(Solution().divideArray(nums,k))