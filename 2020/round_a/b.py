def doit():
  [n, k, p] = [int(x) for x in input().split()]
  status = [-1] * (p+1)
  status[0] = 0
  for _ in range(n):
    stack = [int(x) for x in input().split()]
    for j0 in range(p-1, -1, -1):
      if status[j0] < 0:
        continue
      sum = 0
      for k0 in range(k):
        if j0 + k0 + 1 > p:
          break
        sum += stack[k0]
        if status[j0 + k0 + 1] < status[j0] + sum:
          status[j0 + k0 + 1] = status[j0] + sum
  return status[p]
      

T = int(input())
for t in range(1, T + 1):
  print('Case #{}: {}'.format(t, doit()))
