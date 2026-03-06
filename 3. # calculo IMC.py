# calculo IMC

def calcular_imc (kg, m):
    
    imc = kg/(m**2)

    if imc < 18.5:
        return("Bajo peso", imc) # un return siempre devuelve una tupla, salvo que diga lo contrario
    elif imc >= 18.5 and imc < 25:
        return("Normal", imc)
    elif imc >=25 and imc < 30:
        return("Sobrepeso", imc)
    else:
        return ("obesidad", imc)
    

tipo, valor = calcular_imc(80,1.80)


# IndiceMasaCorporal = calcular_imc(80,1.80)

# asi no se muestra, se mostraria en el programa. Está bien.
# para que se muestre aqui (y podamos comprobar) se hace un print

# print (calcular_imc(80,180))

# print (f"Tiene un IMC {tipo} con un valor de {valor:.2f}")

print (f"Su imc es {calcular_imc(80,1.80)[0]} con un valor de {calcular_imc(80,1.80)[1]}")