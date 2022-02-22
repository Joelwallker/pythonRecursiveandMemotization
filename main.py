def memo(func):
    _cache_ = dict()
    def wrapper(*args):
        if args in _cache_:
            return _cache_[args]
        _cache_[args] = func (*args)
        return _cache_[args]
    return wrapper

@memo
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))