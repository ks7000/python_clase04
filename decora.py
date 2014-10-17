# -*- encoding=utf-8 -*-
import click

def ver(fun):
    def _ver(*args, **kwargs):
        #print u"Bienvenido", fun.__name__
        fun(*args, **kwargs)
        #print u"Adiós", fun.__name__
    return _ver

@ver
@click.command()
@click.option('--x', default=1, prompt='Introduzca el valor de equis', help='Sumando equis')
@click.option('--y', default=4, prompt='Introduzca el valor de ye', help='Sumando ye')
def sumar(x,y):
    print x+y

if __name__ == '__main__':
    sumar()
    #sumar(1, 4)

