class Solution {
    public void merge(int []nums, int low,int mid, int high)
    {
        int [] newArray=new int[high-low+1];
        int index=0;
        int start1=low;
        int end1=mid;
        int start2=mid+1;
        int end2=high;
        while(start1<=end1 && start2<=end2)
        {
            if(nums[start1]<nums[start2])
            {
                newArray[index]=nums[start1];
                start1+=1;

            }
            else 
            {
                newArray[index]=nums[start2];
                start2+=1;
            }
            index+=1;
        }
        while(start1<=end1)
        {
            newArray[index]=nums[start1];
            index+=1;
            start1+=1;
        }
        while(start2<=end2)
        {
            newArray[index]=nums[start2];
            start2+=1;
            index+=1;
        }
        int start=low;
        for(int i=0;i<high-low+1;i++)
        {
            nums[start]=newArray[i];
            start+=1;
        }
    }
    public void mergeSort(int [] nums,int low,int high)
    {
        if(low<high)
        {
             int mid=(low+high)/2;
             mergeSort(nums,low,mid);
             mergeSort(nums,mid+1,high);
             merge(nums,low,mid,high);
        }
    }
    public int[] sortArray(int[] nums) {
        mergeSort(nums,0,nums.length-1);
        return nums;
    }
}
