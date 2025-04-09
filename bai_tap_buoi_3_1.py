'''Write a program that prompts the user to enter base and height of the triangle
and calculate an area of this triangle (area = 0.5 x b x h).
'''
def ex01():
    base  = float(input("Enter base:"))
    height = float(input("Enter hight:"))
    area = (base * height) / 2
    print(f"Area of rectangle: {area}")

'''
Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
Calculate the perimeter of the triangle (perimeter = a + b + c).
'''
def ex02():
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    c = float(input("Enter c:"))
    perimeter = (a + b + c) / 2
    print(f"Perimeter of triangle: {perimeter}")


'''
Get length and width of a rectangle using prompt. Calculate its 
area (area = length x width) and perimeter (perimeter = 2 x (length + width))
'''
def ex03():
    length = float(input("Enter length:"))
    width = float(input("Enter width:"))
    print(f"Area of rectangle: {length * width}")
    print(f"Perimeter of triangle: {2*(length + width)}")

'''
Get radius of a circle using prompt. Calculate the 
area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
'''
import math
def ex04():
    radius = float(input("Enter radius:"))
    print(f"Area of circle: {math.pi*radius**2}")
    print(f"Perimeter of circle: {2*math.pi*radius}")

'''
Calculate the slope, x-intercept and y-intercept of y = 2x -2
'''
def ex05():
    print("Pt y = ax + b")
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    slope = a
    x = -b/a
    y = b
    print(f"Slope: {slope}, x_intercept: {x}, y_intercept: {y}")


'''
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
'''
def ex06():
    x1 = float(input("Enter x1:"))
    y1 = float(input("Enter y1:"))
    x2 = float(input("Enter x2:"))
    y2 = float(input("Enter y2:"))
    slope = (y2 - y1) / (x2 - x1)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"Slope: {slope}, distance: {distance}")

'''
Compare the slopes in tasks 8 and 9. Không hiểu yêu cầu đề bài nên em xin bỏ qua ạ!
'''
def ex07():
    pass

'''
Calculate the value of y (y = x^2 + 6x + 9).
Try to use different x values and figure out at what x value y is going to be 0.
'''
def ex08():
    for x in range(-20, 21):  # Từ -20 đến 20
        y = x ** 2 + 6 * x + 9
        print(f"x = {x}, y = {y}")

        # Kiểm tra nếu y = 0
        if y == 0:
            print(f"--> y bằng 0 khi x = {x}")

'''
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
'''
def ex09():
    print(len("python") != len("dragon"))

'''
Use and operator to check if 'on' is found in both 'python' and 'dragon'
'''
def ex10():
    print('on' is 'python' and 'on' is 'dragon')

'''
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
'''
def ex11():
    sentence = "I hope this course is not full of jargon."

    # Kiểm tra nếu 'jargon' có trong câu
    if "jargon" in sentence:
        print("'jargon' có trong câu.")
    else:
        print("'jargon' không có trong câu.")

'''
Find the length of the text python and convert the value to float and convert it to string
'''
def ex13():
    s = 'python'
    conv = str(len(s))
    print(conv)
'''
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
'''
def ex14():
    num = int(input("Enter your number: "))
    return print("even" if num % 2 == 0 else "odd")
'''
Writs a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
'''
def ex15():
    time_work = float(input("Enter work time:"))
    salary_of_hour = float(input("Enter salary of hour:"))
    print(f"Time work: {time_work}, salary of hour: {salary_of_hour},salary: {time_work * salary_of_hour}")

'''
Write a script that prompts the user to enter number of years.
Calculate the number of seconds a person can live. Assume a person can live hundred years
'''
def ex16():
    age = int(input("Enter age:"))
    print(f"Age: {age}, the number of seconds a person can live: {(100-age)*(365*24*60*60)}")

if __name__ == '__main__':
    ex16()