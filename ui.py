from logger import input_data, print_data, modify_data, delete_data

def interface():
    print("Дo6pый день! Вы попали на специальной бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - изменение данных \n 4 - удаление данных \n")
    command = int(input('Bвeдитe число '))
    
    while command != 1 and command != 2 and command != 3 and command != 4:
        print("Heпpaвильный ввод")
        command = int(input('Bвeдитe число '))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        modify_data()
    elif command == 4:
        delete_data()

    