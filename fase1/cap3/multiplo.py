# PARAMETROS DE ENTRADA:
#
# NUMERO INICIAL: número inicial qualquer
# MULTIPLO: número que representa o fator de multiplicação
# PROXIMO MULTIPLO: o próximo múltiplo do número em MULTIPLO a partir do NUMERO_INICIAL

INICIAL = int(input("Digite um número qualquer: "))
MULTIPLO = int(input("Digite o multiplicador (multiplo): "))

PROXIMO = INICIAL // MULTIPLO * MULTIPLO + MULTIPLO

print("Proximo múltiplo do número {} é {}".format(MULTIPLO, PROXIMO))