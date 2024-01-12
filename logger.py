from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"Вариант №1: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"Вариант №2: \n"
    f"{name}; {surname}; {phone}; {address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число'))
    if var == 1: 
        with open('D:\Материалы к курсу по програмированию\python\S8Task\data_first_variant.csv', 'a', encoding = 'utf-8') as f: 
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n") 
    elif var == 2: 
        with open('D:\Материалы к курсу по програмированию\python\S8Task\data_second_variant.csv', 'a', encoding = 'utf-8') as f: 
            f.write(f"{name}; {surname}; {phone}; {address}\n\n") 

def print_data():
    print('Bывoжy данные из 1 файла: \n')
    with open('D:\Материалы к курсу по програмированию\python\S8Task\data_first_variant.csv', 'r', encoding='utf-8') as f: 
        data_first = f.readlines() 
        data_first_list = [] 
        j = 0 
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]).strip())
        print(''.join(data_first_list))
    
    print('Bывoжy данные из 2 файла: \n')
    with open('D:\Материалы к курсу по програмированию\python\S8Task\data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(''.join(data_second))

def modify_data():
    print('Изменение данных:')
    name = input('Введите имя или фамилию: ')
    with open('D:\Материалы к курсу по програмированию\python\S8Task\data_first_variant.csv', 'r+', encoding='utf-8') as f:
        data = f.readlines()
        f.seek(0)
        for line in data:
            if name in line:
                print('Найденные данные:')
                print(line)
                new_name = input('Введите новое имя: ')
                new_surname = input('Введите новую фамилию: ')
                new_phone = input('Введите новый телефон: ')
                new_address = input('Введите новый адрес: ')
                modified_data = f"{new_name}\n{new_surname}\n{new_phone}\n{new_address}\n\n"
                f.write(modified_data)
                print('Данные изменены успешно.')
                break
            else:
                f.write(line)
            f.truncate() #???

    with open('D:\Материалы к курсу по програмированию\python\S8Task\data_second_variant.csv', 'r+', encoding='utf-8') as f:
        data = f.readlines()
        f.seek(0)
        for line in data:
            if name in line:
                print('Найденные данные:')
                print(line)
                new_name = input('Введите новое имя: ')
                new_surname = input('Введите новую фамилию: ')
                new_phone = input('Введите новый телефон: ')
                new_address = input('Введите новый адрес: ')
                modified_data = f"{new_name}; {new_surname}; {new_phone}; {new_address}\n\n"
                f.write(modified_data)
                print('Данные изменены успешно.')
                break
            else:
                f.write(line)
        f.truncate()

def delete_data():
    print('Удаление данных:')
    name = input('Введите имя или фамилию: ')
    with open('D:\Материалы к курсу по програмированию\python\S8Task\data_first_variant.csv', 'r+', encoding='utf-8') as f:
        data = f.readlines()
        f.seek(0)
        for line in data:
            if name in line:
                print('Найденные данные:')
                print(line)
                print('Данные успешно удалены.')
            else:
                f.write(line) 
        f.truncate()
    
    with open('D:\Материалы к курсу по програмированию\python\S8Task\data_second_variant.csv', 'r+', encoding='utf-8') as f:
        data = f.readlines()
        f.seek(0)
        for line in data:
            if name in line:
                print('Найденные данные:')
                print(line)
                print('Данные успешно удалены.')
            else:
                f.write(line)
        f.truncate()
