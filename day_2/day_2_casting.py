# CASTING: Implicit / Explicit

num1 = 20
num2 = 30.5

print(type(num1))
print(type(num2))

print(num2)
num3 = int(num2)
print(type(num3))
print(num3)

age = input("Tell me your age: ")
print(type(age))
# se tienen que volver a almacenar en la variable, es decir sobre escribirla para que se efectue el casting
print(type(age))
age = int(age)
print(type(age))
new_age = age + 1

print("El siguiente añ tendrás: ")
print(new_age)

#Interesante caso que para sumarlos hay que castearlos de string a su typo exacto , es decir no puede ser int + int, porque ¿Cómo se convierte un string a un int?
num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))

