# -*-encoding:utf-8 -*-
def sumar(fun):
    def _sumar(*args, **kwargs):
        iterador = 0
        for i in args:
            iterador += i
        fun(*args, **kwargs)
        print "Suma de las multiplicandos:", iterador
    return _sumar

@sumar
def multiplicar(*argumentos, **llaves):
    r = 1
    for i in argumentos:
        r = r * i
    print "Multiplicando da:",r

@sumar
def mostrar(*argumentos, **llaves):
    k = 1    
    for i in argumentos:
        print "Mostrando y sumando: item N°", k, " valor:", i
        k +=1

print "-----------"
print "Función 'mostrar(7,11)'"
mostrar( 7, 11)
print
print "-----------"
print "Función 'multiplicar( 7, 11)'"
multiplicar( 7, 11)
