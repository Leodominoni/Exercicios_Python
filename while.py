numero_sorteado = 15
numero_escolhido = input (int('Informe um número até 20: '))
while numero_escolhido != numero_sorteado:
    print('Você errou! Tente novamente')
    numero_escolhido = input (int('Informe um número até 20: '))
print('Acertou')
#if numero_sorteado == numero_escolhido:
#    print('Acertou')
#else:
#   print('Errou')