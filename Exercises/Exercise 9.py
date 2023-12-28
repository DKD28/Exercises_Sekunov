def numbers(number):
    list = ["Ноль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять", "Десять", "Одиннадцать", "Двенадцать"]
    return list[number]

if __name__ == "__main__":
    for i in range(1, 13):
        n = numbers(i)
        print(n)