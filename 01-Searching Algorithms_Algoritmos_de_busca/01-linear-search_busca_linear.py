# Esse algoritmos faz uma busca sequencial comparando a chave elemento a elemento
import os
import platform

def limpar_tela():
    so = platform.system()
    limpar = 'cls' if so == 'Windows' else 'clear'
    os.system(limpar) or None

def busca_linear(chave,lista):
    checagem = 1   
    for i in lista:
        if chave == i:
            return checagem
        checagem += 1
    return 0
 
lista = [8,14,3,26,74,55,28,202,45,7,16,5,47,33,68]

while True:
    limpar_tela()
    try:
        chave = int(input('Digite um valor inteiro a ser pesquisado: '))
        break
    except:
        print('Digite apenas números inteiros para ser buscado!')
        input('Pressione qualquer tecla para continuar')

if busca_linear(chave,lista):
    print(f'Chave encontrada após {busca_linear(chave,lista)} checagens')
else:
    print('Chave não encontrada')