# PROJECT DAY 2 - CALCULAR COMISIONES
# 1. Preguntar al usuario el nombre
# 2. Preguntar al usuario los ingreseos
# 3. Calcular el 13% sin mas de dos decimales
# 4. Informar el porcentaje de comision

# 1
seller_name = input("What\'s your name? ")
#2
income = input("What\'s the sell amount? ")
print("Calculating ...")
#3
income_num = float(income)
print(income_num)
percentage = income_num*13 / 100
percentage_round = round(percentage,2)
#4
print(f"Hey {seller_name}, the percentage of the seller you'll get is {percentage_round}")

#REFACTOR
# 1
seller_name = input("What\'s your name? ")
#2
income = float(input("What\'s the sell amount? "))
print("Calculating ...")
#3
percentage = round(income_num*13 / 100, 2)
#4
print(f"Hey {seller_name}, the percentage of the seller you'll get is {percentage}")