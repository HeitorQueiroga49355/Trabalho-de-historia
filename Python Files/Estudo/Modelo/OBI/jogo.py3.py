n = int(input())
m = n
while True:
  n += m
  m -= 1
  if m == 0: 
    n += 1
    break
print(n)
