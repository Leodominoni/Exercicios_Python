# CONVERSÃO DE TIPOS
idade = '26'
numero1 ='10'
numero2 ='20'
print(numero1 + numero2) #ele nao vai somar ele vai juntar os dois textos pois é uma string
print(idade, type(idade))
idade_inteira = int(idade) #converte para inteiro
print(idade_inteira, type(idade_inteira))
altura = float(input('Informe a sua altura: ')) #todo input é string, mas colocando float vai transformar em float
print(altura, type(altura))
