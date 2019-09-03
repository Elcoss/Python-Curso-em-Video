from time import sleep
n1=int(input('Digite um numero: '))
print('Processando... ')
sleep(1)
if n1%2==0:
    print(f'O numero {n1} e PAR')
else:
    print(f'O numero {n1} e IMPAR')
