A = int(input("Введите число А "))
B = int(input("Введите число В "))
sum_all = 0
sum_chet = 0
sum_nechet = 0
for i in range(A,B+1):
    print(i)
    sum_all = sum(range(A,B+1))
    if i % 2 == 0:
        sum_chet +=i
    if i % 2 != 0:
        sum_nechet +=i
print("Сумма всех чисел равна ", sum_all)
print("Сумма чётных чисел равна ", sum_chet)
print("Сумма нечётных чисел равна ", sum_nechet)

