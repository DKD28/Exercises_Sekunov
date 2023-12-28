def gipotenyza(Katet_1, Katet_2):
    Katet_1 = str(Katet_1)
    Katet_1 = Katet_1.replace(",", ".")
    Katet_1 = float(Katet_1)
    Katet_2 = str(Katet_2)
    Katet_2 = Katet_2.replace(",", ".")
    Katet_2 = float(Katet_2)
    C = ( Katet_1 **2 + Katet_2 ** 2) ** 0.5
    return C


Katet_1 = input("Введите первый катет ")
Katet_2 = input("Введите второй катет ")

C = gipotenyza(Katet_1, Katet_2)
print("Гипотенуза равна ", C)
