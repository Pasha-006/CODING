def isArmstrong(number: int) -> int: 
  digit_count=count_digits(number)
  original_number=number
  newNumber=0
  while number>0:
    reminder=number%10 
    newNumber=newNumber+reminder**digit_count
    number=number//10 
  print(newNumber)
  return newNumber==original_number  
#time complexity O(logN)
#space complexity O(1)
