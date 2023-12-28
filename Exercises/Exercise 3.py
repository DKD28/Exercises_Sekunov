Kilos = (input("Введите массу конфет в кг "))
Kilos = Kilos.replace(",", ".")
Kilos = float(Kilos)
Price = (input("Введите цену конфет "))
Price = Price.replace(",", ".")
Price = float(Price)
Cost = Kilos * Price
print("Стоимость", Kilos, "килограмм конфет равна", round(Cost,2))