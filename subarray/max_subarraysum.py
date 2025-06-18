class Solution(object):
   
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        ans=-10**18  # A large negative number

        sum1=0
        for i in range(0,len(nums)):
            sum1+=nums[i]
            if sum1>ans:
                ans=sum1   
            if sum1<0:
                sum1=0 
          
        return ans"""
        maxSum=nums[0]
        currentMax=maxSum 
        for i in range(1,len(nums)):
            currentMax=max(nums[i],nums[i]+currentMax)
            maxSum=max(currentMax,maxSum)
        return maxSum
