# PROGRMA QUE CALCULA O IMC DE UMA PESSOA


print('CÁLCULO DE IMC')
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m)'))

elevar_2 = altura * altura
imc = peso / elevar_2
print('O imc dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você esta abaixo do peso') 
elif 18.5 <= imc < 25:
    print('Você esta com o peso ideal')
elif 25 <= imc < 30:
    print('Você esta com sobre peso')
elif 30 <= imc < 40:
    print('Você esta com obesidade')
else:
    print('OBESIDADE MÓRBIDA') 
