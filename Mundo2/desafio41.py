from datetime import date
nas=int(input('Que ano vc nasceu: '))
ano=date.today().year-nas
print(f'O atleta tem {ano} anos.')
if ano<=9:
    print('Categoria: Mirim')
elif ano<=14 and ano>9:
    print('Categoria: Infantil')
elif ano<=19 and ano>14:
    print('Categoria: Junior')
elif ano<=25 and ano>19:
    print('Categoria: Senior')
else:
    print('Categoria Master')