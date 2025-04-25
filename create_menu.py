import random



def create_list(n):
    list_random = []
    for i in range(n):
        list_random.append(random.randint(1, 100))
    return list_random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def menu(list_random):
    print('''---------------------------Menu---------------------------
1. In ra danh sách vừa tạo.
2. In đảo ngược danh sách.
3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
4. Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
5. Đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
6. In ra vị trí các phần tử là số nguyên tố.
7. Tìm các số duy nhất (không trùng lặp) trong danh sách.
8. Liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
9. In ra các đoạn con trong danh sách giảm liên tiếp.
10. Thoát''')
    choose = int(input("Chọn lựa của bạn <1..10>:"))
    match choose:
        case 1:
            print(list_random)
        case 2:
            print(list_random[::-1])
        case 3:
            print(sorted(list_random))
        case 4:
            print(f'Phần tử lớn nhất trong danh sách: {max(list_random)}\nVị trí phần tử lớn nhất cuối cùng: {len(list_random) - list_random[::-1].index(max(list_random))}')
        case 5:
            num = int(input('Bạn muốn đếm số nào?:'))
            dem = 0
            index_hien_tai = 0
            vi_tri = []
            for i in list_random:
                if i == num:
                    dem += 1
                    vi_tri.append(index_hien_tai)
                index_hien_tai += 1
            print(f"Phần tử {num} xuất hiện {dem} lần\nTại những vị trí là: {vi_tri}")
        case 6:
            index_hien_tai = 0
            vi_tri = []
            for i in list_random:
                if is_prime(i):
                    vi_tri.append(index_hien_tai)
                index_hien_tai += 1
            print(f"Vị trí xuất hiện của các số nguyên tố: {vi_tri}")
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            exit()

if __name__ == '__main__':
    n = int(input("Nhập số phần tử mảng n: "))
    list_random = create_list(n)
    while True:
        menu(list_random)