'''
Montar frase abaixo com passagem de variáveis :
Declaro para o senhor Gonçalves Dias que o senhor Humberto Delgado esteve presente no evento SecurityCup e gastou o
valor de R$ 30,00 com a entrada.
'''
responsavel=input("Digite o nome do responsável: ")
funcionario=input("Digite o nome do funcionário: ")
evento=input("Digite o nome do Evento: ")
valor=float(input("Digite o valor que será ressarcido: "))
print("Declaro para o Senhor " + responsavel + ", que o senhor " + funcionario + " esteve presente no evento " + evento + " e gastou o valor de R$ " + str(valor) + " com a entrada.")