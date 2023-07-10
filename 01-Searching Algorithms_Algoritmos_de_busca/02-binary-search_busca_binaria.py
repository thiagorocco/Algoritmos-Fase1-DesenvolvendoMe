#Esse algoritmo procura sempre buscar o termo central do array
#O Array precisa estar ordenado em ordem crescente para a busca funcionar corretamente
import os
import platform

def limpar_tela():
    so = platform.system()
    limpar = 'cls' if so == 'Windows' else 'clear'
    os.system(limpar)or None

def busca_binaria(n,lista):
    inicio = 0
    fim = len(lista)
    
    while inicio <= fim:
        meio = inicio + (fim-inicio)//2

        if lista[meio] == n:
            return meio
        elif lista[meio] < n:
            inicio = meio + 1 
        else:
            fim = meio - 1  
    return -1

lista = [2,7,11,16,24,37,42,53,61,67,74,85]

while True:
    limpar_tela()
    try:
        n = int(input('Digite um número a ser pesquisado: '))
        break
    except:
        print('O valor digitado não é um número inteiro')
        input('Pressione qualquer tecla para continuar')

if busca_binaria(n,lista):
    print('Elemento encontrado na posição: ',busca_binaria(n,lista)+1)
else:
    print('Elemento não encontrado')

