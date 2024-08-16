# PROGRAMA QUE PEDE AO USUARIO DOIS VALORES E INDICA QUAL VALOR É MAIOR

num1 = int(input('DIGITE UM NUMERO: '))
num2 = int(input('DIGITE OUTRO NUMERO: '))

if num1 > num2:
    print(f'O primeiro valor é MAIOR')
elif num2 > num1:
    print(f'O segundo valor é MAIOR')
else:
    print('NÃO EXISTE VALOR MAIOR')

