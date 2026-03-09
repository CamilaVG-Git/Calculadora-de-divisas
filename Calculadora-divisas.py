def exchange_money(amount, from_currency, to_currency):
    rates = {
        'USD': 1.0,
        'JPY': 0.0075,
        'EUR': 1.09,
        'MXN': 0.059,
        'DOP': 0.017
    }

    if from_currency not in rates or to_currency not in rates:
        print("Error: moneda no válida.")
        return None
    
    usd = amount * rates[from_currency]

    result = usd / rates[to_currency]
 
    return result

print("Calculadora de divisas")
print("Monedas disponibles: USD, JPY, EUR, MXN")
amount = float(input("Ingresa la cantidad de dinero: "))
from_currency = input("Moneda que tienes: ").upper()
to_currency = input("Moneda a la que quieres convertir: ").upper()

converted = exchange_money(amount, from_currency, to_currency)

if converted is not None:
    print("Resultado:", converted, to_currency)