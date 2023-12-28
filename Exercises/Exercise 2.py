A = int(input("Введите число А "))
B = int(input("Введите число В "))
p = 0
for i in range(A,B+1):
    if A >=B:
        print("Число А больше числа В")
        break
    else:
        print(i)
        p+=1
print ("Общее количество чисел = ", p)