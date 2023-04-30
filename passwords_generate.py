#Генератор паролей
import random
digits = "0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""
num = int(input("Сколько паролей Вы хотите сгенерировать? "))
length = int(input("Какая должна быть длина Вашего пароля? "))
dig = int(input("Включать ли цифры '0123456789'? Да - 1, Нет - 2: "))
u_let = int(input("Включать ли прописные буквы 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'? Да - 1, Нет - 2: "))
l_let = int(input("Включать ли строчные буквы 'abcdefghijklmnopqrstuvwxyz'? Да - 1, Нет - 2: "))
symb = int(input("Включать ли символы '!#$%&*+-=?@^_'? Да - 1, Нет - 2: "))
un_symb = int(input("Исключать ли неоднозначные символы 'il1Lo0O'? Да - 1, Нет - 2: "))



if dig == 1:
    chars += digits
if u_let == 1:
    chars += uppercase 
if l_let == 1:
    chars += lowercase
if symb == 1:
    chars += punctuation
if un_symb == 1:
    chars.replace('il1Lo0O', '')

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

for i in range(num):
    generate_password(length, chars)
    print(generate_password(length, chars))