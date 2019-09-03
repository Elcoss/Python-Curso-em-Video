import math
n1=float(input('Digite o cateto oposto: '))
n2=float(input('Digite o cateto adjacente: '))
n3=(n1*n1)+(n2*n2)
n4=math.sqrt(n3)
print(f'A hipotenusa e {n4:.2f}')