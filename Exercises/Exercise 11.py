def simple():
    number = int(input("Введите число "))
    circle = 0
    for i in range(1, number + 1):
        if number % i == 0:
            circle+=1   
    if circle <=2:
        print("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ) \nЭто простое число")
    if circle > 2:
        print("(ಥ﹏ಥ)(ಥ﹏ಥ)(ಥ﹏ಥ) \nЭто не простое число")


if __name__ == "__main__":
    simple() 