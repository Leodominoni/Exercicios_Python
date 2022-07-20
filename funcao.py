def saudacao():
    print('Bienvenido!')
    print('Gracias')
saudacao()
def saudacao(nome, curso):
    print(f'Bienvenido {nome}!')
    print(f'Gracias por fazer o curso de {curso}')
saudacao('Alisson','Python') 

def saudacao(nome, curso='JavaScript'): #default
    print(f'Bienvenido {nome}!')
    print(f'Gracias por fazer o curso de {curso}')
saudacao('Aline') 

def soma(n1, n2):
    return n1 + n2
resultado = soma(10,3)
print('O resultado é: ', resultado)    