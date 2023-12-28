weight = float(input("Введите свой вес в килограммах "))
height = float(input("Введите ваш рост в сантиметрах "))
height_per_meter = height/100
BMI = weight / (height_per_meter**2)
print("Ваш индекс массы тела равен ", BMI)
if BMI <16:
    print("У вас выраженный дефицит массы тела")
elif BMI >= 16 and BMI <18.5:
    print("У вас недостаточная масса тела")
elif BMI >= 18.5 and BMI <25:
    print("Ваш ИМТ в норме")
elif BMI >= 25 and BMI <30:
    print("У вас избыточная масса тела")
elif BMI >= 30 and BMI <35:
    print("У вас ожирение первой степени")
elif BMI >= 35 and BMI <40:
    print("У вас ожирение второй степени")
elif BMI >=40:
    print("У вас ожирение третьей степени")