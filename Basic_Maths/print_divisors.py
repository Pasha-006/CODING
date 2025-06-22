def printDivisors(number: int) -> None: 
  for i in range(1,number+1):
    if number%i==0:
      print(i) 
#time complexity O(N)
#space complexity O(1)
