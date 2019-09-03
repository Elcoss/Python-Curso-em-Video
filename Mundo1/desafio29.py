n1=int(input('Qual velocidade vc esta: '))
if n1<=80:
    print('Tenha um bom dia, dirija com seguran;a')
else:
    n2=(n1-80)*7
    print(f'MULTADO! Vc execedeu o limite permitido que e de 80km/h \n'
          f'Voce deve pagar uma multa de {n2:.2f}')
