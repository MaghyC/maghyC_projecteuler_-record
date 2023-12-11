import numpy as np 
import math


def findNthPrime(n): 
  if n <= 0:
    return 
  if n==1:
    return 2
  count=1
  k=3
  primeLis= np.array([])
  
  while count<n:
    if is_Prime_Lis(primeLis,k):
      primeLis= np.append(primeLis,k)
      count+=1
    k+=2
  return k-2
    
def is_Prime_Lis(lis, n):
  if n <= 1:
    return False
  for i in lis:
    if n%i==0:
      return False
    if i*i>n:
      return True
  return True
    

def findPrimeIn(n):
  if n<2:
    return []
  if n==2:
    return np.array([2]) 
  arr = np.repeat([True], int(n / 2))
  lis = np.array([2]) 
  i = 3
  while i < n:
    if arr[int(i / 2)]:
      lis = np.append(lis, i)
      for _ in range(i, int(n / i) + 1, 2):
        arr[int(i * _ / 2)] = False
    i += 2
  return lis

