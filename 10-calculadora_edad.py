# Haz una calculadora de edad exacta (años, meses, dias)


import datetime

ano = int(input("Introduce su año de nacimiento: "))
mes = int(input("Introduce su mes de nacimiento: "))
dia = int(input("Introduce su dia de nacimiento: "))

fecha_nac = datetime.date(ano,mes,dia)

hoy = datetime.date.today()

edad = hoy - fecha_nac





