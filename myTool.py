import numpy as np 
import math


# tools    
def factorization(n):
  if n<2:
    return {}
  
  i = 2
  k=0
  dict={}
  while i < n/2+1:
    if n%i==0:
      dict.update({f'{i}': 0}) 
      temp_n_b=int(math.log(n,i)+1)
      for _ in range(1, temp_n_b  ):
        if n%i==0:
          n/=i
          dict[f'{i}']=dict[f'{i}']+1
    i+=1
  if dict == {}:
    dict={f'{n}':1}
  return dict
  
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
  

#fProblem_5
def findLCM(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return 2
  ans = 1
  primeLis = findPrimeIn(n)
  k = 0
  while int(math.log(n, primeLis[k])) > 1:
    i = primeLis[k]
    power = int(math.log(n, i))
    ans = ans * pow(i, power)
    k += 1
    i = primeLis[k]
  for _ in range(k, len(primeLis)):
    ans *= primeLis[_]
  return ans
  
#Problem_6
def D_N_SUMOS_SOSUM(n):
  SUMOS=0
  SOSUM=0
  for i in range(n+1):
    SUMOS+=pow(i,2)
    SOSUM+=i
  SOSUM=pow(SOSUM,2)
  return SOSUM-SUMOS
  
#Problem_7
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

#Problem_8
def n_digit_largest_product_in_series(n,series_init):
  series_init=series_init.replace("\n", "")
  series_init=series_init.replace(" ", "")
  N=len(series_init)
  if n > N:
    return
  series=np.array([int(digit) for digit in series_init])
  max_product=np.prod(series[0:n])
  i=0
  k=n-1
  while k<N:
    conti=True
    if series[k]==0:
      i+=n
      k+=n
      conti=False
    if series[i]==0:
      conti=False
    if conti:
      temp=np.prod(series[i:k+1])
      if temp>max_product:
        max_product=temp
    i+=1
    k+=1
  return max_product

#Problem_9
def find_a_b_c_eq_n(n):
  
  c_xia=int(n/3)
  
  sq=np.array([])
  alis=np.array([])
  for c in range(1,int(n/2+1)):
    c_2=c**2
    alis=np.append(alis,c)
    sq=np.append(sq,c_2)
    abc=None
    if c> c_xia:
      for i in range(len(sq)):
          for j in range(i+1,len(sq)):
            if (sq[i]+sq[j])==c_2 and alis[i]+alis[j]+c==n:
              abc=alis[i]*alis[j]*c

return abc

#Problem_10
#sum(findPrimeIn(n))


    


