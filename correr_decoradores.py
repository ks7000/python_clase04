import decoradores
valor = decoradores.logger(decoradores.sigma)
valor ( 3, 5, 7)

valor_dos = decoradores.sigma( 8, 2, 9)
print valor_dos , "valor_dos"
mi_valor = decoradores.logger(valor_dos)
print mi_valor , "mi_valor"

