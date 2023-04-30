#Шифр Цезаря

n = int(input("Какое направление выберете: шифрование - 1, дешифрование - 2? "))
lang = int(input("Выберите язык алфавита: русский - 1, английский - 2: "))
step = int(input("Выберите шаг сдвига: "))

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


if n == 1:
    text = input("Введите текст, который нужно зашифровать: ")
    new_text = []
    if lang == 1:
        for i in text:
            if i.isupper() == True:
                ind = rus_upper_alphabet.index(i)
                new_text.append(rus_upper_alphabet[ind+step])
            elif i.islower() == True:
                ind = rus_lower_alphabet.index(i)
                new_text.append(rus_lower_alphabet[ind+step])
            else:
                new_text.append(i)
    if lang == 2:
        for i in text:
            if i.isupper() == True:
                ind = eng_upper_alphabet.index(i)
                new_text.append(eng_upper_alphabet[ind+step])
            elif i.islower() == True:
                ind = eng_lower_alphabet.index(i)
                new_text.append(eng_lower_alphabet[ind+step])
            else:
                new_text.append(i)
    new_text = ''.join(new_text)
    print(new_text)

elif n == 2:
    text = input("Введите текст, который нужно дешифровать: ")
    new_text = []
    if lang == 1:
        for i in text:
            if i.isupper() == True:
                ind = rus_upper_alphabet.index(i)
                new_text.append(rus_upper_alphabet[ind-step])
            elif i.islower() == True:
                ind = rus_lower_alphabet.index(i)
                new_text.append(rus_lower_alphabet[ind-step])
            else:
                new_text.append(i)
    if lang == 2:
        for i in text:
            if i.isupper() == True:
                ind = eng_upper_alphabet.index(i)
                new_text.append(eng_upper_alphabet[ind-step])
            elif i.islower() == True:
                ind = eng_lower_alphabet.index(i)
                new_text.append(eng_lower_alphabet[ind-step])
            else:
                new_text.append(i)
    new_text = ''.join(new_text)
    print(new_text)

