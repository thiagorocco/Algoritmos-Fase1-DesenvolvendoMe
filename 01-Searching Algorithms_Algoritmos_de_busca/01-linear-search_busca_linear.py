lista = [8,14,3,26,74,55,28,202,45,7,16,5,47,33,68]

while True:
    try:
        chave = int(input('Digite um valor inteiro a ser pesquisado: '))
        break
    except:
        print('Digite apenas números inteiros para ser buscado!')

checagem = 1
encontrado = False

for i in lista:
    if chave == i:
        print(f'Chave {chave} encontrada na {checagem}.a checagem')
        encontrado = True
        break
    checagem += 1

if not encontrado:
    print('Chave não encontrada na lista')