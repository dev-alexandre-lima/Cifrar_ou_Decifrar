#Esse código ele vai cifrar e decifrar algumas letras e ver a ordem
#texto válido para continuar o programa
def texto_valido():
    texto = "S"
    return texto
#Cifrar as letras
def cifrar():
    #letra da entrada
    print("Ditige a mensagem com letras em maiúsculas:")
    mensagem = input().upper()
    cifrar_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decifrar_1 = "POIUYTREWQLKJHGFDSAZXCVBNM"
    resultado = "".upper()
    for i in range(len(mensagem)):
        #comparar a letra da mensagem com a letra cifrada
        comparar = cifrar_1.index(mensagem[i])
        #vai adicionar a letra cifrada na variável resultado
        resultado += decifrar_1[comparar]
    print("Resultado: ", resultado)
#Decifrar a letras
def decifrar():
    #letra da entrada
    print("Ditige a mensagem com letras em maiúsculas:")
    mensagem = input().upper()
    cifrar_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decifrar_1 = "POIUYTREWQLKJHGFDSAZXCVBNM"
    resultado = "".upper()
    for i in range(len(mensagem)):
        #comparar a letra da mensagem com a letra decifrada
        comparar = decifrar_1.index(mensagem[i])
        #vai adicionar a letra decifrada na variável resultado
        resultado += cifrar_1[comparar]
    print("Resultado: ", resultado)
#menu de opções
def menu():
    texto = texto_valido().upper()
    while texto == "S":
        #Opções do menu
        print("1 - Cifrar")
        print("2 - Decifrar")
        print("3 - Sair S/N")
        texto_1 = input().upper()
        if texto_1 == "1":
            cifrar()
        elif texto_1 == "2":
            decifrar()
        #Opção para continuar ou não
        print("Deseja continuar? S/N:")
        texto = input()
    return
menu()
