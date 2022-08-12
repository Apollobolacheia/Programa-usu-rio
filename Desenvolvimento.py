from datetime import date


data = str(date.today()).split("-") #lista de strings que recebe valores de data da biblioteca datetime

i = 0
while i == 0: 
    try:
        nome_usuario = input("Digite seu nome completo: ")                                 #recebe nome
        if len(nome_usuario.split(" ")) > 1:                                               #tratamento de erro para nome incompleto
            ano_usuario = int(input("Digite o ano que você nasceu, se entre 1922-2021: ")) #recebe ano
            if ano_usuario >= 1922 and ano_usuario <= 2021:                                #tratamento de erro para intervalo de ano defido
                idade = int(data[0]) - ano_usuario                                         #calcula idade do usuário
                i = 1
            else:
                print("Por favor digite um ano válido entre 1922 e 2021")                  #Mensagem de erro para o ano incorreto
        else:
            print("Por favor digite o nome completo!")                                     #Mensagem de erro para o nome incorreto
    except ValueError:
        print("Por favor digite um ano válido entre 1922 e 2021")                          #Mensagem de erro para valores string na variável ano_usuario


print("Olá {}, se você ja completou aniversário esse ano, você tem {} anos".format(nome_usuario, idade))
#print("Olá seja Bem Vindo ",nome_usuario, - idade)