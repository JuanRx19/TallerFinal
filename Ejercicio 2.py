par1 = eval(input("Digite la nota del Parcial 1: "))
par2 = eval(input("Digite la nota del Parcial 2: "))
taller = eval(input("Digite la nota del Taller: "))
proye = eval(input("Digite la nota del Proyecto: "))
nf = (((par1+par2)*25)/100)+((taller*20)/100)+((proye*30)/100)
print("La nota final es: " + str(nf))