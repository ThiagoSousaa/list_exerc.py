# PROGRMA QUE LEIA O ANO DE NASCIMENTO DE UMA ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM SUA IDADE

ano_atual = int(input('Digite o ano atual: '))
ano_nascimemto = int(input('Digite o ano de seu nascimento: '))

idade = ano_atual - ano_nascimemto 
print(f'VOCE TEM {idade} anos')
if idade <= 9:
    print('ATLETA MIRIM')
elif idade <= 14 and idade > 9:
    print('ATLETA INFANTIL')
elif idade <= 20 and idade > 14:
    print('ATLETA JÚNIOR')
elif idade > 20:
    print('ATLETA SÊNIOR')
else:
    (False)