height = (float(input("Digite sua Altura: ")))
weight = (float(input("Digite o seu Peso: ")))
imc = weight/(height**2)
if imc < 17:
     print("Muito abaixo do peso")
elif imc >= 17 and imc < 18.5:
      print ("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
      print("Peso Ideal")
elif imc >= 25 and imc <30:
    print("SobrePeso")
elif imc>= 30 and imc < 35:
    print("Obesidade")
elif imc >= 35 and imc < 40:
   print("Obesidade Severa")