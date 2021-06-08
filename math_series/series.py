def fibonacci(n):
  if(type(n) != int):
    return 'not an integer'
  if (n <= 1):
    return n
  return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
  if(type(n) != int):
    return 'not an integer'
  if (n == 0):
    return 2
  elif (n == 1):
    return n
  return lucas(n-1) + lucas(n-2)

def sum_series(n,b=0,c=1):
  if(type(n) != int or type(b) != int or type(c) != int):
    return 'not an integer'
  if( b==0 and c == 1):
    return fibonacci(n)
  elif (b == 2 and c == 1):
    return lucas(n)
  else:
    if (n == 0):
      return b
    elif (n == 1):
      return c
    