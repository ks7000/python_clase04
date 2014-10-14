def ver(fun):
    def _ver(*args, **kwargs):
        print "Bienvenido", fun.__name__
        fun(*args, **kwargs)
        print "Adios", fun.__name__
    return _ver

@ver
def sumar(x,y):
    print x+y

sumar(1, 4)

