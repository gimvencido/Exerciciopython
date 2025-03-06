# Imprima uma mensagem de boas-vindas na tela.
print( "Seja Bem vindo!")

# Declare uma variável booleana verdadeiro com o valor True e imprima seu tipo

verdadeiro = True
print(type(verdadeiro))

#Imprima o resultado da multiplicação de dois números decimais de sua escolha
#print(cumprimento, nome, 'Sua senha é %s'%(senha))
n1 = 10
n2 = 15
resultado = n1 * n2
print('n1, n2, resultado é  %s'%(resultado))

#4 Imprima o resultado da divisão de dois números inteiros 
nume1 = 2
nume2 = 5
print(nume1 + nume2)

#5 Imprima o resultado da subtração de dois números inteiros de sua escolha
nu1 = 30
nu2 = 10
print( nu1 - n2)

#6 Imprima o resultado da divisão inteira de dois números inteiros 
numero1 = 400
numero2 = 200
print(numero1 / numero2)


#7 Imprima o resultado da multiplicação de 4 números decimais de sua escolha

numero3 = 2
numero4 = 6
numero5 = 8
numero6 = 12
result =  (numero3 * numero4 * numero5 * numero6 )

print(f'   resultado é {resultado}')


# Declare uma variável numero e atribua um número inteiro. Em seguida, imprima o dobro desse número

number = 20
print(number * number)

#9 Crie uma calculadora de soma com as ferramentas que vc já conhece(Use apenas input, print e variavel)
#print(f'{cumprimento} {nome} Sua senha é {senha}')
soma1 = float(input(" Digite um numero:")) 
soma2 = float(input("Digite outro numero:"))
print (soma1 + soma2)

multi1= float(input(" Digite um numero:")) 
multi2 = float(input(" Digite um numero:")) 
print(multi1 * multi2)

divi1 = float(input(" Digite um numero:")) 
divi2 = float(input(" Digite um numero:")) 
print(divi1 / divi2)

subi1= float(input(" Digite um numero:")) 
subi2 = float(input(" Digite um numero:")) 
print( subi1 - subi2)

#10 Crie um sistema de cadastro com as estruturas que vc já conhece(Use apenas input, print e variavel)
# print(cumprimento, nome,'Sua senha é',senha)
nome = input("Digite seu nome")
idade= int(input("Digite sua idade"))
pets = bool(input("Tem pets?"))
print(nome, idade, pets )
