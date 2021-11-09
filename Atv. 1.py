print('Atividade 1\n##############')
dias = int(input("Idade em dias :"))
anos = dias//365
meses = (dias % anos) // 30
dias = (dias % 365) % 30
print("{0} ano(s), {1} mes(es), {2} dia(s)".format(anos, meses, dias))