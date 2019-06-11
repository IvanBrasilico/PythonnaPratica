raw = r'String \t \'raw \n  exemplo\' '
print(raw)

str = 'String \t \'normal. \n   exemplo\''
print(str)

lista = ['String', 'joined', '.']
str2 = ' '.join(lista)
print(str2)
print(str2.split())

str3 = ','.join(lista)
print(str3)
print(str3.split(','))

num = 1
facil = u'fácil'
dificil = u'difícil'

print('%d. Formatacao de frases %s ou %s? ' % (num, facil, dificil))

num = 2
print('{num}. Formatacao de frases {facil} ou {dificil}? '.format(
    num=num, facil=facil, dificil=dificil))

num = 3
import sys

if sys.version_info[0] == 3 and sys.version_info[1] > 5:
    print(f'{num}. Formatacao de frases {facil} ou {dificil}? ')

bytestr = str2.encode()
print(bytestr)
print(bytestr.decode('utf-8'))


# pitfall
def print_items_lista(umalista: list):
    """Imprime os itens de uma lista em linhas

    :param umalista: lista de strings
    """
    for linha in umalista:
        print(linha)


print_items_lista(lista)
print_items_lista(str3[:5])

print(len(str3))
print(len(lista))
try:
    print(lista.index('X'))
except ValueError as err:
    print(err)
print(str3.find('X'))
print(str3.index('X'))
