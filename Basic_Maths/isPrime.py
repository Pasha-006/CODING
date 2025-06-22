import math
def isPrime(number : int) -> bool:
  divisorsCount=0
  for i in range(1,int(math.sqrt(number))+1): 
    if number%i==0:
      divisorsCount+=1 
  if divisorsCount==1:
    return True 
  return False
#time complexity o(sqrt(N))
#space complexity O(1)
