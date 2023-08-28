phone_book = {}
PATH = 'Python_Seminars\PhoneBook.txt'


def open_file(book: dict):
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        book[i] = contact


def show_contacts(book: dict, message: str):
    print('\n' + '='*67)
    if book:
        for i, contact in book.items():
            print(f'{i}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
        print('='*67 + '\n')
    else:
        print(message)
        print('='*67 + '\n')
    
    
def add_new_contact(book: dict, new: list):
    cur_id = ((max(book.keys()) + 1) if book.keys() else 1)
    book[cur_id] = new


def save_file(book: dict):
    all_contacts = []
    for contact in book.values():
        all_contacts.append(';'.join(contact))
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(all_contacts))


def find_contact(book: dict, search: str):
    result = {}
    for i, contact in book.items():
        for field in contact:
            if search.lower() in field.lower():
                result[i] = contact
                break
    return result


def func_search(book: dict):
    search = input('Что будем искать? ')
    result = find_contact(phone_book, search)
    show_contacts(result, f'Контакт содержащий {search} не найден!')


def change_contact(book: dict, contact_id: int):
    name, phone, comment = book.get(contact_id)
    ch = []
    for item in ['Введите новое имя (или оставьте пустым, чтобы не изменять)',
                 'Введите телефон (или оставьте пустым, чтобы не изменять)',
                 'Введите коммент (или оставьте пустым, чтобы не изменять)']:
        ch.append(input(item))
    book[contact_id] = [ch[0] if ch[0] else name, ch[1] if ch[1] else phone, ch[2] if ch[2] else comment]
    return ch[0] if ch[0] else name
    

def delete_contact(book: dict, contact_id: int):
    name = book.pop(contact_id)
    return name[0]


def menu():
    menu_points = ['Открыть файл',
                   'Сохранить файл',
                   'Посмотреть все контакты',
                   'Добавить контакт',
                   'Найти контакт',
                   'Изменить контакт',
                   'Удалить контакт',
                   'Выход']
    print('Главное меню:\n')
    [print(f'\t{i}. {item}') for i, item in enumerate(menu_points, 1)]
    choise = int(input('\nВыберите пункт меню: '))
    return choise


while True:
    choise = menu()
    match choise:
        case 1:
            open_file(phone_book)
            print('\nТелефонная книга успешно открыта!\n')
        case 2:
            save_file(phone_book)
            print('\nТелефонная книга успешно сохранена!\n')
        case 3:
            show_contacts(phone_book, 'Телефонная книга пуста или не открыта!')
        case 4:
            new = []
            for item in ['Введите имя: ', 'Введите телефон: ', 'Введите коммент: ']:
                new.append(input(item))
            add_new_contact(phone_book, new)
            print(f'\nКонтакт {new[0]} успешно добавлен!\n')
        case 5:
            func_search(phone_book)
        case 6:
            func_search(phone_book)
            select = int(input('Какой контакт будем изменять? '))
            name = change_contact(phone_book, select)
            print(f'\nКонтакт {name} успешно изменен!\n')
        case 7:
            func_search(phone_book)
            select = int(input('Какой контакт будем удалять? '))
            name = delete_contact(phone_book, select)
            print(f'\nКонтакт {name} успешно удален!\n')
        case 8:
            print('\nВсего хорошего!')
            break