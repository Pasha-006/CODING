def count_digits(number : int)->int:
    count=0
    while number!=0:
      number=number//10
      count+=1
    return count
#time complexity log(number)
#space complexity O(1)
