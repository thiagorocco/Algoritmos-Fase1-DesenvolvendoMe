#Esse algoritmo procura sempre buscar o termo central do array
#O Array precisa estar ordenado em ordem crescente para a busca funcionar corretamente

def busca_binaria(n):
    print()

lista = [2,7,11,16,24,37,42,53,61,67,74,85]

while True:
    try:
        n = int(input('Digite um número a ser pesquisado: '))
        break
    except:
        print('O valor digitado não é um número inteiro')

try:
    busca_binaria(n)
except:
    print('Algo deu errado.')

