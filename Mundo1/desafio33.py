a=int(input('Primeiro valor: '))
b=int(input('Segundo valor: '))
c=int(input('Terceiro valor: '))
m=a
if b<a and b<c:
    m=b
if c<b and c<a:
    m=c
ma=a
if b>a and b>c:
    ma=b
if c>b and c>a:
    ma=c
print(f'Maior valor foi {ma}')
print(f'Menor valor foi {m}')
