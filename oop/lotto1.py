import random

def auto_lotto():
    # numbers = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    numbers = [i for i in range(1, 46)]
    random.shuffle(numbers)
    return numbers

def main():
    print(auto_lotto())

if __name__ == '__main__':
    main()

# 절차 지향 프로그래밍
# OOP