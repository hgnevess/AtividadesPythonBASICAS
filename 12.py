parcial1 = int(input("digite a primeira nota parcial "))
parcial2 = int(input("digite a segunda nota parcial "))

media = (parcial1 + parcial2) / 2

if media == 10:
  print("Aprovado com distinção")
elif media >= 7:
  print("Aprovado")
else:
  print("Reprovado")

