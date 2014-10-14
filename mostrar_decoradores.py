from decoradores import logger
@logger
def sigma(*args):
    return sum([i for i in args])
