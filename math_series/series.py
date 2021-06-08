def fibonacci(n):
  if(type(n) != int):
    return 'not an integer'
  return sum_series(n, 0, 1)

def lucas(n):
  if(type(n) != int):
    return 'not an integer'
  return sum_series(n, 2, 1)
  # if (n == 0):
  #   return 2
  # elif (n == 1):
  #   return n
  # return lucas(n-1) + lucas(n-2)

def sum_series(n,b=0,c=1):
  if(type(n) != int or type(b) != int or type(c) != int):
    return 'not an integer'
  if (n == 0):
    return b
  elif (n == 1):
    return c
  return sum_series(n-1,b,c) + sum_series(n-2,b,c)