# -*- encoding=utf-8 -*-
import click
import decoradores

@click.command()
@click.option( '--valor1', default=3, prompt='Introduzca el valor1 por favor', help='Valor1 es necesario')
@click.option( '--valor2', default=5, prompt='Introduzca el valor2 por favor', help='Valor2 es necesario')
@click.option( '--valor3', default=7, prompt='Introduzca el valor3 por favor', help='Valor3 es necesario')
def muestra_valor( valor1, valor2, valor3):
    valor = decoradores.logger(decoradores.sigma)
    #valor ( 3, 5, 7)
    valor ( valor1, valor2, valor3)

if __name__ == '__main__':
    muestra_valor()

#valor_dos = decoradores.sigma( 8, 2, 9)
#print valor_dos , "valor_dos"
#mi_valor = decoradores.logger(valor_dos)
#print mi_valor , "mi_valor"

