def timed(func):
    def inner(*args, **kwargs):
        name = str(func)
        print "Starting ", name, "..."
        result = func(*args, **kwargs)
        print name, " ended."
        return result
    return inner
