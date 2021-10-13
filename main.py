def myF1(a,b):
  print(a,b)
  return a #stops here, ignores the rest
  print('AFTER') 

x = myF1(1,2)

def myF(a,b):
  print(a,b)
  if a<b:
      return 'a is smaller'
  if b<a:
      return 'b is smaller'
  return 'equal'

x = myF(1,1)
print('X:',x)
