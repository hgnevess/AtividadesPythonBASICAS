numero1 = float (input('Digite o primeiro numero'))
numero2 = float (input('Digite o segundo numero'))
numero3 = float (input('Digite o terceiro numero'))
if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero3 and numero2 > numero1:
    print(numero2)
else:
    print(numero3)