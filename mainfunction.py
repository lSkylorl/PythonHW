import json
import os

def chooseDataType():
    typeData = None
    flag = True
    while flag:
        print('Выбирете какие данные добавить: ', '1 - mobilephone', '2 - workphone', '3 - email', '4 - birthday', sep='\n')
        typeData = input('Выбирете тип телефона: ')
        match typeData:
            case '1':
                typeData = 'mobilephone'
                flag = False
            case '2':
                typeData = 'workphone'
                flag = False
            case '3':
                typeData = 'email'
                flag = False
            case '4':
                typeData = 'birthday'
                flag = False
            case _: flag = True
    return typeData

def menu():
    print('пункты меню: ',
          '0 → выход из программы',
          '1 → сохранение в удаленном хранилище',
          '2 → загрузка данных из удаленного хранилища',
          '3 → поиск по ФИО всех данных контакта',
          '4 → поиск по ФИО телефоны',
          '5 → вывод всех контактов',
          '6 → создать новый контакт',
          '7 → удалить контакт',
          '8 → редактировать контакт',
          '9 → добавить контактые данные', sep='\n')

def save(phoneBook):
    os.system('cls||clear')
    with open('phone_book.json', 'w', encoding='utf-8') as x:
        x.write(json.dumps(phoneBook, ensure_ascii=False, indent=4))
    print('\nСохранение... Телефонная книга успено сохранена.\n')

def load():
    os.system('cls||clear')
    with open('phone_book.json', 'r', encoding='utf-8') as x: pbLocal = json.load(x)
    print('\nЗагрузка... Телефонная книга успешно загружена.\n')
    return pbLocal

def searchAllDataContact():
    pbLocal = load()
    printAllFullname()
    arg = pbLocal.get(input("Полность введите ФИО для поиска всех данных: ").lower().strip(), None)
    if arg != None:
        for i, j in arg.items():
            if type(j) == list:
                for i in range(len(j)):
                    print(i, j[i], sep=' ', end='\n')
            else:
                print(i, j)
    else:
        print('\nОшибка! Такого контакта в телефонной книге не существует')
    print()

def searchPhonesContact():
    pbLocal = load()
    printAllFullname()
    arg = pbLocal.get(input("Полностью введите ФИО для поиска всех телефонных контактов: ").lower().strip(), None)
    if arg != None:
        for i, j in arg.items():
            if (i == 'mobilephone' or i == 'workphone'):
                for i in range(len(j)):
                    print(i, j[i], sep=' ', end='\n')
    else: print('\nОшибка! Такого контакта в телефонной книге не существует')
    print()

def printAllFullname():
    os.system('cls||clear')
    pbLocal = load()
    print("Список контактов в телефонной книге:")
    [print(' ', i) for i in pbLocal.keys()]
    print()

def createNewContant():
    pbLocal = load()
    printAllFullname()
    print('Введите ФИО нового контакта по образцу: Фамилия Имя Отчество')
    arg = input("Введите ФИО: ").lower().strip()
    if arg in pbLocal:
        return print('\nТакой контакт уже существует! Выбирете пункт меню 9 → добавить контактые данные\n')

    typeData = chooseDataType()

    inputData = input("Введите данные: ")
    pbLocal.update({arg: {'mobilephone': [], 'workphone': [], 'email': [], 'birthday': []}})
    pbLocal[arg][typeData].append(inputData)
        
    save(pbLocal)
    print('Контакт создан и данные добавлены!\n')

def deleteContact():
    pbLocal = load()
    printAllFullname()

    print('\nВведите ФИО по образцу: Фамилия Имя Отчество')
    arg = input("ФИО контака который нужно удалить: ").lower().strip()
    answer = pbLocal.get(arg, None)
    if answer != None:
        pbLocal.pop(arg)
        save(pbLocal)
        print('Контакт успешно удалён.\n')
    else: print('\nТакого контакта в телефонной книге не существует!\n')

def editContact():
    pbLocal = load()
    printAllFullname()

    arg = input("Введите ФИО контакта который нужно отредактировать: ").lower().strip()
    answer = pbLocal.get(arg, None)
    if answer != None:
        count = 0
        dictRes = {}
        print('\nСписок данных доступных для редактирования: ')
        for i, j in pbLocal[arg].items():
            if len(j) > 0:
                for i in j:
                    dictRes[count] = [i, i]
                    print(count, i, i)
                    count += 1         
            else:
                dictRes[count] = [i, j]
                print(count, i, j)
                count += 1

        typeData = None
        flag = True
        while flag:
            typeData = int(input('Выбирете данные которые хотите редактировать: '))
            if dictRes.get(typeData, 0) != 0:
                try: position = pbLocal[arg][dictRes[typeData][0]].index(dictRes[typeData][1])
                except: position = -1

                if position >= 0: pbLocal[arg][dictRes[typeData][0]][position] = input('Введите новые данные: ')
                else: pbLocal[arg][dictRes[typeData][0]] = [(input('Введите новые данные: '))]

                flag = False
            
        save(pbLocal)
        print('Контакт отредактирован\n')
    else: print('\nТакого контакта в телефонной книге не существует!\n')

def addDataContact():
    pbLocal = load()
    printAllFullname()

    arg = input("Выберите в какой контакт хотите добавить данные: ").lower().strip()   
    typeData = chooseDataType()
    inputData = input("Введите данные для добавления: ")
    if type(pbLocal[arg][typeData]) == list: pbLocal[arg][typeData].append(inputData)
    else: pbLocal[arg][typeData] = inputData
        
    save(pbLocal)
    print('\nНовые данные успешно добавлены\nТелефонная книга успено сохранена.\n')