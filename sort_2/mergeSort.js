/**
 * @param {number[]} nums
 * @return {number[]}
 */

function merge(nums,low,mid,high)
{
    let array=[];
    let start1=low;
    let end1=mid;
    let start2=mid+1;
    let end2=high;
    while( start1<=end1 && start2<=end2)
    {
        if(nums[start1]<nums[start2])
        {
            array.push(nums[start1]);
            start1+=1;
        }
        else 
        {
            array.push(nums[start2]);
            start2+=1;
        }
    }
    while(start1<=end1)
    {
        array.push(nums[start1]);
        start1+=1;
    }
    while(start2<=end2)
    {
        array.push(nums[start2]);
        start2+=1;
    }
    let start=low;
    for(let i=0;i<array.length;i++)
    {
        nums[start]=array[i];
        start+=1;

    } 
}

function mergeSort(nums,low,high)
{

    if(low<high)
    {
        let mid=Math.floor((low+high)/2);
        mergeSort(nums,low,mid);
        mergeSort(nums,mid+1,high);
        merge(nums,low,mid,high);
    }
}

var sortArray = function(nums) {

    mergeSort(nums,0,nums.length-1);
    return nums;
    
};
