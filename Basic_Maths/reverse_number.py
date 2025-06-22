def reverse_number(number : int) -> int: 
  sign=-1 if number<0 else 1
  number=number*sign
  reversed_number=0 
  while number!=0:
    reminder=number%10
    reversed_number=reversed_number*10+reminder 
    number=number//10 
  return reversed_number*sign
#time complexity O(log N)
#space complexity O(N)
