print('Atividade 1\n##############')
a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))

if a > b + c:
    print('Os valores apresentados podem formar um triângulo!\n\n#############\nCalculo da área\n#############\n')
    base = int(input('Digite o valor da base do triângulo: '))
    altura = int(input('Digite o valor da altura do triângulo :'))
    area = (base * altura) / 2
    print('Area = {0}'.format(area))
else:
    print('Os valores apresentados não podem formar um triângulo!')