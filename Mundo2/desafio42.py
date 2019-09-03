n1=float(input('Digite um lado do triangulo: '))
n2=float(input('Digite outro lado do triangulo: '))
n3=float(input('Digite mais um lado do triangulo: '))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    if n1==n2==n3:
        print('Os lados acima PODEM FORMA um triangulo Esquilatero')
    elif n1==n2 or n1==n3 or n2==n3:
        print('Os lados acima PODEM FORMA um triangulo Isoceles')
    else:
        print('Os lados acima PODEM FORMA um triangulo Escaleno')
else:
    print('Os lados acima NAO PODEM FORMA um triangulo')