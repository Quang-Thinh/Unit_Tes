def MyBigNumber(stn1: str, stn2: str):
  i = len(stn1) - 1
  j = len(stn2) - 1
  rem = 0
  sum = []
  while i >= 0 or j >= 0 :
    if i >= 0:
      n1 = int(stn1[i])
    else:
      n1 = 0
    if j >= 0:
      n2 = int(stn2[j])
    else:
      n2 = 0
    sum_n = n1 + n2 + rem
    rem = sum_n // 10
    sum.append(str(sum_n % 10))
    i -= 1
    j -= 1
  return "".join(sum[::-1])