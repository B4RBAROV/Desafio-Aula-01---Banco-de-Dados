import time

bd = open('dados_clientes.dbf', 'r')
name = input('name: ')

print('\n------- User Name: {} -------\n'.format(name))

linha = bd.readline()
cont = 1
inicio = time.perf_counter()
while linha != '':
    if name in linha:
        print('{}. {}'.format(cont, linha))
        cont += 1
    linha = bd.readline()
fim = time.perf_counter()

tempo = fim - inicio
print('Tempo de Busca: {:.4f} seg'.format(tempo))
