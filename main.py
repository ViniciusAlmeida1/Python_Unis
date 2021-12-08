import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="sortee_local",
    password="sortee",
    database="imc"
)

mycursor = mydb.cursor()


def menu():
    print("""
        [1] - Calcular IMC 
        [2] - Listar pacientes
        [3] - Sair
    """)

menu()
opcao = int(input("Escolha uma opção: "))


if opcao == 1:
    nome_paciente = str(input("Digite o nome do paciente: "))
    peso_paciente = float(input("Digite o peso do paciente(KG): "))
    altura_paciente = float(input("Digite a altura do paciente(CM): "))

    imc = round((peso_paciente ** 2) / altura_paciente)

    if imc < 17:
        print("\nIMC = {} Muito abaixo do peso!".format(imc))
        descricao_imc = "Muito abaixo do peso"
    elif 17 <= imc <= 18.49:
        print("\nAbaixo do peso!")
        descricao_imc = "Abaixo do peso"
    elif 18.50 <= imc <= 24.99:
        print("\nPeso normal!")
        descricao_imc = "Peso normal"
    elif 25 <= imc <= 29.99:
        print("\nAcima do peso!")
        descricao_imc = "Acima do peso"
    elif 30 <= imc <= 34.99:
        print("\nObesidade I")
        descricao_imc = "Obesidade I"
    elif 35 <= imc <= 39.99:
        print("\nObesidade II")
        descricao_imc = "Obesidade II"
    else:
        print("\nObesidade III")
        descricao_imc = "Obesidade III"

    print("\nGravando dados...")

    sql = "INSERT INTO paciente (nome_paciente, altura_paciente, peso_paciente, imc_paciente, descricao_imc_paciente) " \
          "VALUES (%s, %s, %s, %s, %s)"
    val = (nome_paciente, altura_paciente, peso_paciente, imc, descricao_imc)
    mycursor.execute(sql, val)

    mydb.commit()

elif opcao == 2:

    mycursor.execute("SELECT * FROM paciente")
    resultado = mycursor.fetchall()

    for i in resultado:
        print(i)

elif opcao == 3:
    print("Programa Finalizado!")
