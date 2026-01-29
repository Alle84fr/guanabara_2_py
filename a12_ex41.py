#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

from datetime import date

years = int(input("ano: "))

years_now = date.today().year

age = years_now - years

if age <= 9 : print("Mirim")
elif age <= 14 : print("Infatil")
elif age <= 19 : print("Júnior")
elif age <= 25 : print("Sênior")
else: print("Master")