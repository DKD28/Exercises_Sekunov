point = input("Введите балл землетрясения ")
point = point.replace(",", ".")
point = float(point)
if point <2:
    print("Минимальное зелетрясение")
elif 2<= point < 3:
    print("Очень слабое землетрясение")
elif 3<= point < 4:
    print("Слабое землетрясение")
elif 4<= point < 5:
    print("Промежуточное землетрясение")
elif 5<= point < 6:
    print("Умеренное землетрясение")
elif 6<= point < 7:
    print("Сильное землетрясение")
elif 7<= point < 8:
    print("Очень сильное землетрясение") 
elif 8<= point < 10:
    print("Огромное землетрясение")
elif point >=10:
    print("Разрушительное землетрясение")