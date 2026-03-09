def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


rates = {
    "JPY": 0.0075,
    "EUR": 1.09,
    "MXN": 0.059,
    "DOP": 0.017
}

print("Calculadora de divisas")
print("Monedas disponibles: JPY, EUR, MXN, DOP")

budget = float(input("Ingresa la cantidad en USD: "))
currency = input("Moneda a la que quieres convertir: ").upper()

if currency in rates:
    exchange_rate = rates[currency]
    result = exchange_money(budget, exchange_rate)
    print("Resultado:", result, currency)
else:
    print("Error: moneda no válida")