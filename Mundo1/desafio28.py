from random import randint
from time import sleep
cpu=randint(0,5)
print('-=-'*20)
print('Vou pensa em um numero entre 0 e 5. tente adivinha...')
print('-=-'*20)
j1=int(input('Em qual numero pensei: '))
print('Processando...')
sleep(2)
if j1==cpu:
    print('Parabens vc ganhou')
else:
    print(f'Vc errou eu pensei no {cpu} e n no {j1}')
