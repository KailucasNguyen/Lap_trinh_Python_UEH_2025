'''
Write a program that prints numbers from 1 to 10
'''
def ex01():
    for i in range(1, 11):
        print(i)
'''
Write a program to calculate the sum of numbers in a range from 1 to n (n is entered from the keyboard)
'''
def ex02():
    n = int(input("Enter n:"))
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(f"Sum of numbers in range 1 to {n}: {sum}")

'''
Write a program to calculate the sum of even (/odd) numbers in a range from 1 to n (n is entered from the keyboard)
'''
def ex03():
    n = int(input("Enter n:"))
    sum_even = 0
    sum_odd = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    print(f"Sum of even numbers in range 1 to {n}: {sum_even}")
    print(f"Sum of odd numbers in range 1 to {n}: {sum_odd}")
'''
Write a program to check how many vowels are in a string entered from the keyboard.
'''
def ex04():
    s = input("Enter a string:")
    vowels = "aeiouAEIOU"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    print(f"Number of vowels: {count}")
'''
Write a program to count the number of words in a sentence the user enters.
'''
def ex05():
    sentence = input("Enter a sentence:")
    words = sentence.split()
    print(f"Number of words: {len(words)}")
'''Write a program that implements a game as the following description:

	1. The computer generates a random number from 1 to 100

	2. The user was asked to guess

	3. match the user-guessing number to the generated number
'''
import random
def ex06():
    num_random = random.randint(1, 101)
    lv = input("Mời bạn nhập mức độ trò chơi (E/M/H): ")
    times = 0
    match lv:
        case "E":
             times = 10
        case "M":
             times = 6
        case "H":
             times = 4
    for i in range(times):
        num_guess = int(input("Enter your guessing number:"))
        if num_guess == num_random:
            print(f"You win! After {i+1} times.")
        elif num_guess > num_random:
            print(f"Wrong! Your guessing number is too high. you have {times-i-1} times left.")
        else:
            print(f"Wrong! Your guessing number is too low. you have {times-i-1} times left.")
    print(f"The computer's guessing number is {num_random}")

if __name__ == '__main__':
    ex06()