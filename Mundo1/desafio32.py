from datetime import date
n1=int(input('Digite um ano, ou digite 0 para analisar o seu ano: '))
if n1==0:
    n1=date.today().year
if n1%4==0 and n1%100!=0 or n1%400==0:
    print(f'{n1} E um ano bissesto')
else:
    print(f'{n1} N e um ano bissesto')
