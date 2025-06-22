def isPalindrome(number : int) -> bool: 
  sign =-1 if number<0 else 1 
  if sign ==-1 :
    return False 
  reversed_number=reverse_number(number)
  return reversed_number==number 
#time complexity O(logN)
#space complexity O(1)
