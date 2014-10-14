# -*-encoding:utf-8 -*-
def sumar(fun):
    def _sumar(*args, **kwargs):
        print "-----------"
        print " Función ",fun.__name__,"(",
        k = 1        
        for i in args:
            print i,
            if k < len(args):
                print ",",
            k += 1
        print ")"
        iterador = 0
        for i in args:
            if isinstance(i,int):            
                iterador += i
            else:
                print "(argumento no válido, se obvia :",i,")"
        fun(*args, **kwargs)
        print "Suma de las multiplicandos:", iterador
        print
    return _sumar

@sumar
def multiplicar(*argumentos, **llaves):
    r = 1
    for i in argumentos:
        if isinstance(i,int):        
            r = r * i
    print "Multiplicando da:",r

@sumar
def mostrar(*argumentos, **llaves):
    k = 1    
    for i in argumentos:
        if isinstance(i,int):        
            print "Mostrando y sumando: item N°", k, " valor:", i
            k +=1

mostrar( 7, "Hola", 0.23, 12, 20)
multiplicar( 7, "Hola", 0.23, 12, 20)
