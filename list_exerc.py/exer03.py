# PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORMA DE ACORDO COM SUA IDADE, SE ELE TERÁ QUE SE ALISTAR, SE ELE PRECISA DE ALISTAR OU SE ELE JA PASSOU DA HORA DE SE ALISTAR

ano_nascimento = int(input('Em que ano você nasceu? '))
ano_atual = int(input('Em que ano estamos? '))

idade = ano_atual - ano_nascimento
print(f'Você tem {idade} anos')

if idade > 18:
    print('Você já passou do tempo de se alistar')
elif idade == 18:
    print('Você tem que se alistar')
elif idade < 18:
    print('Você ainda vai se alistar no serviço militar')
else:
    (False)



