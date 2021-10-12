def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



"""def fibonacci(n):
  fib = [0,1]
  for i in range(2,n+1):
    fib.append(fib[i-1] + fib[i-2])
  return fib[n]"""