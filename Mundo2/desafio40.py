n1=float(input('Qual a primeira nota: '))
n2=float(input('Qual a segunnda nonta: '))
m=(n1+n2)/2
print(f'Tirando {n1} e {n2} a media do aluno e {m:.1f}')
if m>=7:
    print('O aluno foi aprovado')
elif m<7 and n1>=4 or n2>=4:
    print('O aluno esta de recupera;ao')
elif n1<4 and n2<4:
    print('o aluno esta reprovado')