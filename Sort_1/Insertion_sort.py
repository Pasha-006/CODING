def insertion_sort(numbers: list[int])->None: 
   for i in range(1,len(numbers)): 
        while i>0 and numbers[i-1]>numbers[i]:
            numbers[i-1],numbers[i]=numbers[i],numbers[i-1] 
            i-=1 
   print(numbers)
#time complexity 0(n^2)
# space complexity O(1)
