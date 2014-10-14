def sumar(fun):
    def _sumar(*args, **kwargs):
        iterador = 0
        for i in args:
            iterador += i
        fun(*args, **kwargs)
        print "Suma de las multiplicaciones:", iterador
    return _sumar

@sumar
def multiplica(*argumentos):
    r = 1
    for i in argumentos:
        r = r * i
    print r

@sumar
def muestra(*argus):
    k = 1    
    for i in argus:
        print "mostrando", k, i

multiplica(1, 2, 3, 4, 5, 7, 89)

muestra( 3, 2, 2, 4)
