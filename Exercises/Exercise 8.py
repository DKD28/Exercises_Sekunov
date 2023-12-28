def taxi(km):
    km = km.replace(",", ".")
    km = float(km)
    path = km * 1000 / 140
    cost = 240 + 15 * path
    return round(cost)

cost = taxi(input("Введите расстояние поездки в километрах "))
print(cost)
