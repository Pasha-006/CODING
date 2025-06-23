def selection_sort(numbers: list[int])->None:
  for i in range(len(numbers)): 
    min=i 
    for j in range(i+1,len(numbers)): 
      if numbers[j]<numbers[min]:
        min=j 
    numbers[i],numbers[min]=numbers[min],numbers[i]
#time complexity 0(n^2)
# space complexity O(1)
