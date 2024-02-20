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
  n=n+1
  if n < 2:
    return []
  if n == 2:
    return np.array([2])
  arr = np.repeat([True], int(n / 2))
  lis = np.array([2])
  i = 3
  while i <n:
    if arr[int(i / 2)]:
      lis = np.append(lis, i)
      for _ in range(i, math.ceil(n/i), 2):
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

#problem_11
def find_20x20_multi(string):
lis_1 = string.replace('\n', " ").split(' ')
lis = []
max = 1
temp=1
count = 0

for i in range(0, 20):
  j=0
  while j < 20:
    str = lis_1[i * 20 + j]
    if str[0] == "0":
      lis.append(int(str[1]))
    else:
      lis.append(int(str))
    j+=1

for i in range(3,20):
  for j in range(0,20):
    temp= lis[(i-3)*20+j]*lis[(i-2)*20+j]*lis[(i-1)*20+j]*lis[(i)*20+j]
    if max<temp:
      max=temp
    temp=lis[i-3+j*20]*lis[i-2+j*20]*lis[i-1+j*20]*lis[i+j*20]

    if max<temp:
      max=temp
i=0
while i<17:
  j=i
  while j<17:
    temp=lis[i*20+j]*lis[(i+1)*20+j+1]*lis[(i+2)*20+j+2]*lis[(i+3)*20+j+3]
    if max<temp:
      max=temp
    temp=lis[i*20+20-j]*lis[(i+1)*20+20-j-1]*lis[(i+2)*20+20-j-2]*lis[(i+3)*20+20-j-3]
    if max<temp:
      max=temp
    j+=1
  i+=1
print(lis)
print(max)

#Problem_12
def Highly_Divisible_Triangular_Number(N):
  th = 1
  num = 1
  divisor_num = 1
  while divisor_num < N:
    divisor_num = 1
    th += 1
    num += th
    prime_lis = findPrimeIn(th + 1)
    dic = {key: 0 for key in prime_lis}
    temp_n_1 = th + 1
    temp_n_0 = th
    for p in prime_lis:
      while temp_n_1 % p == 0:
        dic[p] += 1
        temp_n_1 = temp_n_1 // p
      while temp_n_0 % p == 0:
        dic[p] += 1
        temp_n_0 = temp_n_0 // p
    dic[2] = dic[2] - 1
    for key in dic:
      divisor_num = divisor_num * (dic[key] + 1)
  return num


def Longest_Collatz_Sequence(N): #Problem_14
  max_length = 1
  sta = 1
  arr = np.zeros(N)
  arr[0] = 1

  def find_length_collatz_sequence(n):
    if (len(arr) > n) and (arr[n - 1] != 0):
      return arr[n - 1]
    if n % 2 == 0:
      res = find_length_collatz_sequence(n // 2) + 1
    else:
      res = find_length_collatz_sequence(3 * n + 1) + 1
    if len(arr) >= n:
      arr[n - 1] = res
    return res

  for i in range(1, N):
    res = find_length_collatz_sequence(i)

    if max_length < res:
      max_length = res
      sta = i
  return sta



    

def Lattice_Paths(x, y, n): #Problem_15
    n=n+1
    #lat=np.zeros(n*n)
    
    lat=[0]*(n*n)
    lat[n*n-1]=1
    def find_Lattice_Paths(x, y):# Problem_15
       
        if x>n-1 or y>n-1:
            return 0
    

        if lat[x*n+y]!= 0:
            return lat[x*n+y]
        lat[x*n+y]=find_Lattice_Paths(x+1, y) +find_Lattice_Paths(x, y+1)
        return lat[x*n+y]
    
    return find_Lattice_Paths(x, y)


def number_to_words_1000(n): #Problem_17
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ones[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + "hundred"
        else:
            return ones[n // 100] + "hundredand" + number_to_words(n % 100)
    else:
        return "onethousand"

def Maximum_Path_Sum_I(text):#Problem_18
    arr=text.split("\n")
    lis= list(map(int, arr[-1].split(" ")))
    for _ in range(2,len(arr)+1):
        temp=list(map(int, arr[-_].split(" ")))
        for i in range(0,len(temp)):
            temp[i]=temp[i]+max(lis[i],lis[i+1])
        lis=temp
    return lis[0]

def Counting_Sundays_1901_2000()::#Problem_19
  yearid = 1900
  monthid = 1
  dayofmonth = 7
  sunonfirst = 0
  
  def daysinmonth(year, month):
      if month in [4, 6, 9, 11]: return 30
      if month == 2:
          if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): return 29
          else: return 28
      return 31
  
  while yearid <= 2000 and monthid <= 12 and dayofmonth <= 31:
      dim = daysinmonth(yearid, monthid)
      if dayofmonth == 1 and yearid > 1900: sunonfirst += 1
      dayofmonth += 7
      if dayofmonth > dim:
          dayofmonth -= dim
          monthid += 1
          if monthid == 13:
              monthid = 1
              yearid += 1
  return sunonfirst


def sum_of_divisors(n): #Problem_21
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)
