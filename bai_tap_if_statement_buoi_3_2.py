def ex_01():
    age = int(input("Enter your age: "))
    return print("person is eligible for voting") if age >= 18 else print("person is not eligible for voting")

def ex_02():
    num = int(input("Enter your number: "))
    return print("even" if num % 2 == 0 else "odd")

def ex_03():
    num = int(input("Enter your number: "))
    return print("Divisible by 7" if num % 7 == 0 else "Not divisible by 7")

def ex_04():
    num = int(input("Enter your number: "))
    last_num = num % 10
    return print(f"Số cuối cùng của {num} chia hết cho 3" if last_num % 3 == 0 else f"Số cuối cùng của {num} không chia hết cho 3")

import random
def ex_05():
    num = int(input("Mời bạn nhập số mà bạn đoán (từ 1 đến 9): "))
    num_random = random.randint(1, 9)
    if num_random == num:
        print("Chúc mừng bạn đã đoán đúng")
    else:
        print(f"Bạn đã đoán sai, số chính xác là: {num_random}")

def ex_06():
    num = int(input("Enter your number [1..7]: "))
    if num == 1:
        print("Sunday")
    elif num == 2:
        print("Monday")
    elif num == 3:
        print("Tuesday")
    elif num == 4:
        print("Wednesday")
    elif num == 5:
        print("Thursday")
    elif num == 6:
        print("Friday")
    else:
        print("Saturday")

if __name__ == '__main__':
    ex_05()
