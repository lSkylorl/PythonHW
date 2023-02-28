from mainfunction import *

try:
    phoneBook = load()
except:
    phoneBook = {
        "иванов иван иванович": {"mobilephone": ["79505159014", "79629274774"], "birthday": ["21-11-1984"], "email": ["foxinc@yandex.ru"]},
        "сергеев сергей сергеевич": {"mobilephone": ["79059361721", "79861129862"], "birthday": ["19-08-2000"], "email": ["sergio@yandex.ru"]}}
    save(phoneBook)
    print("Попытка загрузки телефонной книги... Не удалось загрузить телефонную книгу! Создние тестовой телефонной книги.\n")

choice = None
while choice != 0:
    menu()
    choice = int(input("Введите в консоль пункт меню: "))
    match choice:
        case 0: print('\nВыполняется выход из программы... До скорых встреч!')
        case 1: save(phoneBook)
        case 2: load()
        case 3: searchAllDataContact()            
        case 4: searchPhonesContact()
        case 5: printAllFullname()
        case 6: createNewContant()
        case 7: deleteContact()
        case 8: editContact()
        case 9: addDataContact()