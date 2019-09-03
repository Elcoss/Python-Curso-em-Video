peso=float(input('Quantos kg vc pesa: '))
alt=float(input('Qual a sua altura: '))
imc=peso/(alt**2)
print(f'O IMC dessa pessoa e de {imc:.1f}')
if imc<=18.5:
    print('Abaixo do Peso')
elif imc<=24.9:
    print('Peso Normal')
elif imc<=30:
    print('Sobrepeso')
elif imc<=40:
    print('Obesidade')
else:
    print('obesidade morbida')