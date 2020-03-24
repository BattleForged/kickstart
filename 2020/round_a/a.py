def doit():
  [n, m] = [int(x) for x in input().split()]
  x = [int(x) for x in input().split()]
  x.sort()
  i = 0
  while m >= 0 and i < n:
    m -= x[i]
    i += 1
  return i if m >= 0 else i - 1
      

T = int(input())
for t in range(1, T + 1):
  print('Case #{}: {}'.format(t, doit()))
