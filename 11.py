salario=float(input("Digite o seu salário:"))


if salario <=280 :
  aumento=(salario*0.20)
  novosalario=(aumento+salario)
  print("Salário antes do reajuste", salario)
  print("O percentual de aumento aplicado foi de: 20%")
  print(f"O valor do aumento foi de: {aumento:.2f}")
  print("O novo salário é de:", novosalario)

elif salario >280<700 :
  aumento1=(salario*0.15)
  novosalario1=(aumento1+salario)
  print("Salário antes do reajuste", salario)
  print("O percentual de aumento aplicado foi de: 15%")
  print(f"O valor do aumento foi de:  {aumento1:.2f}")
  print("O novo salário é de:", novosalario1)

elif salario >700<1500 :
  aumento2=(salario*0.10)
  novosalario2=(aumento2+salario)
  print("Salário antes do reajuste", salario)
  print("O percentual de aumento aplicado foi de: 10%")
  print(f"O valor do aumento foi de: {aumento2:.2f}")
  print("O novo salário é de:", novosalario2)

elif salario >1500:
  aumento3=(salario*0.05)
  novosalario3=(aumento3+salario)
  print("Salário antes do reajuste", salario)
  print("O percentual de aumento aplicado foi de: 5%")
  print(f"O valor do aumento foi de: {aumento3:.2f}")
  print("O novo salário é de:", novosalario3)