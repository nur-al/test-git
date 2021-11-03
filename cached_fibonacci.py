def cache(fn):
    cache = {}
    def wrapper(n):
        nonlocal cache
        if n not in cache:
            cache[n] = fn(n)
            #print(f'Adding result to cache:{cache[n]}')
        #print(f'cache = {cache}')
        return cache[n]
    return wrapper

def fibonachi(n):
    if n < 2:
        return n
    else:
        return fibonachi(n-1) + fibonachi(n-2)


cached_fib = cache(fibonachi)
cached_fib(4)

print('======================================')
@cache
def fibonachi(n):
    if n < 2:
        return n
    else:
        return fibonachi(n-1) + fibonachi(n-2)

fibonachi(3)