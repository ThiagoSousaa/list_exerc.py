''' == CONDIÇÕES ALINHADAS === '''

# Programa que indica se o empréstimo bancário será aprovado ou não

print('CALCULE SEU EMPRÉSTIMO\n')

# OBETENDO VALORES PARA ANÁLISE DO EMPRÉSTIMO

valor_casa = float(input('Qual o valor da casa? '))
salario_mensal = float(input('Qual o valor de seu salário? '))
anos_pagamento = int(input('Em quantos anos deseja pagar? '))

# CALCULANDO VALORES

total_parcelas = anos_pagamento * 12    
print(f'total de parcelas {total_parcelas}')


valor_prestacao = valor_casa / total_parcelas
print(f'O valor da prestação mensal é de {valor_prestacao}')


limite_prestacao = salario_mensal *0.30
print(f'O valor maximo da prestação permitido é de {limite_prestacao}')

analisando_dados = print('analisando dados')

if valor_prestacao <= limite_prestacao:
    print('EMPRÉSTIMO APROVADO')
else:
    print('EMPRÉSTIMO NEGADO')

