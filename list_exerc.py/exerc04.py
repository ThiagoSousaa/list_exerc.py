# CALCULAR A MEDIA DE UM ALUMO, ACIMA DE 5 APROVADO, ABAIXO DE 5 REPROVADO

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

nota_final = nota1 + nota2

if nota_final < 5:
    print(f'Sua nota final é {nota_final}, VOCÊ FOI REPROVADO')
elif nota_final < 5 or 6.9.__format__:
    print(f'Sua nota final é {nota_final}, EM RECUPERAÇÃO')
elif nota_final >= 5:
    print(f'Sua nota final é {nota_final}, VOCÊ FOI APROVADO')

    