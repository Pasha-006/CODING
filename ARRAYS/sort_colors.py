class Solution(object):
    def sortColors(self,a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        mid=0
        high=len(a)-1
        while mid<=high:
            if a[mid]==0:
                a[left],a[mid]=a[mid],a[left]
                left+=1 
                mid+=1 
            elif a[mid]==1:
                mid+=1 
            else:
                a[mid],a[high]=a[high],a[mid]
                high-=1
    
        
