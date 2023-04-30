#Числовая угадайка

def game():
    print("Добро пожаловать в числовую угадайку")
    print("Укажите диапазон чисел: от 1 до...")
    import random
    a = int(input())
    x = random.randint(1, a)
    def is_valid(num):
        if 1 <= num <= a:
            return True
        else:
            return False

    counter = 0

    while True:
        print("Введите цифру от 1 до ", a, ":")
        n = int(input())
        if is_valid(n) == False:
            print("А может быть все-таки введем целое число от 1 до 100?")
        else:
            if n < x:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                counter += 1
                print("Количество попыток: ", counter)
            elif n > x:
                print("Ваше число больше загаданного, попробуйте еще разок")
                counter += 1
                print("Количество попыток: ", counter)
            elif n == x:
                print("Вы угадали, поздравляем!")
                counter += 1
                print("Количество попыток: ", counter)
                print("Хотите продолжить? Да - 1, Нет - 2")
                f = int(input())
                if f == 1:
                    counter = 0
                    game()
                else:
                    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
                    exit()

game()


