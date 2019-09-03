l=' LOJAS GUANABARA '
print(f'{l:=^40}')
p=float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] a vista cartao')
print('[ 3 ] 2x no cartao')
print('[ 4 ] 3x ou mais no cartao')
f=int(input('Qual a sua escolha? '))
if f==1:
    print('Voce recebeu um desconto no valor de 10%')
    d10=(p/100)*10
    print(f'Sua compra de R${p:.2f} vai custar R${p-d10:.2f} no final.')
elif f==2:
    print('Voce recebeu um desconto no valor de 5%')
    d5=(p/100)*5
    print(f'Sua compra de R${p:.2f} vai custar R${p-d5:.2f} no final.')
elif f==3:
    print(f'Sua compra sera parcelada em 2x de R${p/2:.2f} SEM JUROS')
    print(f'E custara um total de R${p:.2f}.')
elif f==4:
    par=int(input('Quantas Parcelas? '))
    if par<3:
        print('Selecione o outro metodo de pagamento'
              '\nEsse metodo so e valido para 3x ou mais parcelas.')
    if par>=3:
        j20=(p/100)*20
        print('A sua compra tera um total de 20% de juros')
        print(f'Sua compra sera parcelada em {par}x de R${(p+j20)/par:.2f} COM JUROS')
        print(f'Sua compra de R${p:.2f} vai custar R${(p+j20):.2f} no final.')
else:
    print('Escolha um numero de 1 a 4.')