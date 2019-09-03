from datetime import date
a=int(input('Ano de nascimento: '))
ano=date.today().year
print(f'Quem nasceu em {a} tem {ano-a} anos em {ano}')
if ano-a<18:
    print(f'ainda faltam {18-(ano-a)} anos para o alistamento')
    print(f'Seu alistamento sera em {a+18}')
elif ano-a>18:
    print(f'Voce ja deveria ter se alistado ha {(ano-a)-18} anos')
    print(f'seu alistamento foi em {a+18}')
elif ano-a==18:
    print('Voce deve se alistar imediatamente')
