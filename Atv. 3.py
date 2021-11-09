print('Atividade 3\n##############')

valor_1 = int(input("Digite um valor: "))
valor_2 = int(input("Digite outro valor: "))
valor_3 = int(input("Digite mais um valor: "))

menor_valor = valor_1

if(valor_2 < menor_valor):
    menor_valor = valor_2
if(valor_3 < menor_valor):
    menor_valor = valor_3

print('\nO menor valor digitado foi: {0}'.format(menor_valor))