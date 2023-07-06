#Esse algoritmo procura sempre buscar o termo central do array
#O Array precisa estar ordenado em ordem crescente para a busca funcionar corretamente
import os
import platform

def limpar_tela():
    so = platform.system()
    limpar = 'cls' if so == 'Windows' else 'clear'
    os.system(limpar)or None

def busca_binaria(n,lista):
    fim = len(lista)
    inicio = 0
    meio = fim/2

    checagens = 1
    while True:
        if n == lista[meio]:
            return checagens
        elif n > lista[meio]:
            meio
        else:
            inicio 


lista = [2,7,11,16,24,37,42,53,61,67,74,85]

while True:
    limpar_tela()
    try:
        n = int(input('Digite um número a ser pesquisado: '))
        break
    except:
        print('O valor digitado não é um número inteiro')
        input('Pressione qualquer tecla para continuar')

busca_binaria(lista,n)

