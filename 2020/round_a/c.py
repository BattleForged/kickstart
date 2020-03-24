def test(maxM, m):
  if maxM == 0:
    return 10**10
  need = 0
  for lesson in m:
    need += (lesson-1) // maxM
  return need

def doit():
  [n, k] = [int(x) for x in input().split()]
  m = [int(x) for x in input().split()]
  for i in range(n-1, 0, -1):
    m[i] = m[i] - m[i-1]
  m.pop(0)
  l0 = 0
  r0 = max(m)
  while (l0 < r0):
    mid = (l0+r0) // 2
    need = test(mid, m)
    if need <= k:
      r0 = mid
    else:
      l0 = mid + 1
  return l0
      

T = int(input())
for t in range(1, T + 1):
  print('Case #{}: {}'.format(t, doit()))
