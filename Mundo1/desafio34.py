n1=float(input('Qual o valor do seu salario? R$'))
n2=(n1/100)*15
if n1>=1250:
    n2=(n1/100)*10
print(f'O seu salario reajustado sera {n1+n2:.2f}R$')