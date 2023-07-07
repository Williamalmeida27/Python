print("Ola mundo!")

##Tipos em python:

print(11 + 10) ## saída é um tipo int
int() 
print(11.5 + 10.5) ## saída é um tipo float
float()
print(True) ## saída é um tipo bool  
bool()
print("11 + 10") ## saída é um tipo str 

##Executando o python no terminal python ou python -i app.py

##Funções dir e help:

#dir() ## Retorna uma lista de nomes do escopo local
#dir(100) # Retorna todos os metódos que o tipo int 100 tem.

#help() #Sistema de ajuda.
##help(100)

##Boas Práticas:

idade , nome = 28, 'William'

print(nome, idade)

nome_completo = (nome, 'Almeida Santos') ##Padrão snake  case
print(nome_completo)

BRAZILIAN_STATES = ['sp', 'rj'] ##Constante em python sempre maiúscula
print(BRAZILIAN_STATES)

#Saída:
#William 28
#('William', 'Almeida Santos')
#['sp', 'rj']

##Ordem de precência:

print((10 * 2) + 10 / 2)

##Bloco em Python: Existe uma convenção de usar 4 espaços:

def sacar(valor: float):
    saldo = 500

    if saldo >= valor:
        print("Saldo sacado!")


def depositar(valor: float):
    saldo = 500
    saldo += valor
    return saldo

sacar(200)
print(depositar(500))

##No python else if é contraido elif
opcao = int(input("Informe uma opção: 1 | 2"))
if opcao == 1:
    print("Opcao 1")
elif opcao == 2:
    print("Opção 2")
else:
    print("Opção inválida")
    quit()
    

##Condicional aninhada:

conta_normal = True
conta_universitaria = False

saldo = 500
saque = 0

if conta_normal:
    seleciona = int(input("Informe uma opção 1 - Saque /n 2 - Extrato"))

    if seleciona == 1:
        saque = float(input("Valor a ser sacado?"))
        if saque >= saldo:
            print(f'O valor de R$ {saque} foi sacado')

        else:
            print("Saldo insulficiente")            
    elif seleciona == 2:
        print('Seu saldo atual é {saldo}')
    else:
        print("Opção invalida")
        quit()
elif conta_universitaria:
    seleciona = int(input("Informe uma opção 1 - Saque /n 2 - Extrato"))

    if seleciona == 1:
        saque = float(input("Valor a ser sacado?"))
        if saque >= saldo:
            print(f'O valor de R$ {saque} foi sacado')

        else:
            print("Saldo insulficiente")            
    elif seleciona == 2:
        print('Seu saldo atual é {saldo}')
    else:
        print("Opção invalida")
        quit()
else:
    quit()

##If ternario:
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque")


##Estrutura de repetição: For e While:

texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

##range é uma função bultin do python, gera um object range:
#O range quem um inicio start, fim end, e os passos setp

range(4) ##Saida: range(0,4)
##Agora podemos converte um range object em list com posições:

list(range(4)) ##Saida: [0, 1, 2, 3]

#Usando range com for:
for numero in range(0, 11):
    print(numero, end='')
##Sainda: 0 1 2 3 4 5 6 7 8 9 10

#Usando o conceito de inicio, fim e passos:
for tabuada in range(0, 51, 5):
    print(tabuada, end='') ##O end ao fim, deixamos um ao lado do outro
##Saida: 0 5 10 15 20 25 30 35 40 45 50

##Usando o while, o enquanto é usado quando não sabemos o número exato de vezes a ser repetido:

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] sair"))

    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Extrato")

##Dominando strings:
#remover espaços em brancos em um texto usa o strip ou lsstrip/rstrip
#centralizar e juntar:curso = "PYTHON" curso.center(10, #): ##Python##
#Juntar: (".".join(curso)): "P.Y.T.H.O.N"

#Testar alguns metódos de strings:
print(nome.upper())
print(nome.lower())
print(nome.title())

##String multiplo: f""" """"

mensagem = f"""
    Teste {nome}
        teste2
"""