class Solution:
    def merge(self,nums,low,mid,high):
        newArray=[]
        index=0
        start1=low
        end1=mid
        start2=mid+1 
        end2=high
        while start1<=end1 and start2<=end2:
            if nums[start1]<nums[start2]:
                newArray.append(nums[start1])
                start1+=1 
            else:
                newArray.append(nums[start2])
                start2+=1
        while start1<=end1:
            newArray.append(nums[start1])
            start1+=1 
        while start2<=end2:
            newArray.append(nums[start2])
            start2+=1 
        start=low
        for i in range(0,high-low+1):
            nums[start]=newArray[i]
            start+=1 
    def mergeSort(self,nums,low,high):
        if low<high:
            mid=(low+high)//2 
            self.mergeSort(nums,low,mid)
            self.mergeSort(nums,mid+1,high)
            self.merge(nums,low,mid,high)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums
        
