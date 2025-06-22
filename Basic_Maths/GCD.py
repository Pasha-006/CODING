def HCF(number1: int, number2: int) ->int: 
  if number2>number1: 
    number1,number2=number2,number1 
  while number2>0:
     number1,number2=number2, number1%number2
  return number1 
#time complexity O(logN)
#space complexity O(1)
