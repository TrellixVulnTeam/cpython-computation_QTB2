def removename(func):
    func.__name__= ''
    return func
    
def setnewName(name):
    def decorator(func):
        func.__name__ = name
        return func
    return decorator

print(removename())    