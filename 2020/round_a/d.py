def maxPreLen(a, b):
  r = min(len(a), len(b))
  for i in range(r):
    if a[i] != b[i]:
      return i
  return r

class UFSet:

  def __init__(self):  
    self.father = self
    self.unused = 1
  
  def isTop(self):
    return self.father == self
  
  def top(self):
    if self.father == self:
      return self
    self.father = self.father.top()
    return self.father
  
  def combine(self, other):
    otherTop = other.top()
    top = self.top()
    if otherTop == top:
      return
    top.unused += otherTop.unused
    otherTop.father = top
  
  def use(self, x):
    top = self.top()
    times = top.unused//x
    top.unused -= x * times
    return times



def doit():
  [n, k] = [int(x) for x in input().split()]
  strList = []
  times = n // k 
  for i in range(n):
    strList.append(input())
  strList.sort()
  # print(strList)

  actionStack = []
  for i in range(n-1):
    actionStack.append((maxPreLen(strList[i], strList[i+1]), i))
  actionStack.sort(reverse=True)
  # print(actionStack)

  ans = 0
  setList = [UFSet() for i in range(n)]
  for i in range(n-1):
    (ansx, where) = actionStack[i]
    setList[where].combine(setList[where+1])
    t = setList[where].use(k)
    if t > 0:
      times -= t
      ans += t * ansx
    if times == 0:
      return ans

  return ans//0
      

T = int(input())
for t in range(1, T + 1):
  print('Case #{}: {}'.format(t, doit()))
