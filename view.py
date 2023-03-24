import csv

def greatings():
    print('Добро пожаловать!')


def menu():
    print()
    print('Телефонный справочник\n Выберите действие: \n 1. Показать весь список \n 2. Добавить запись\n 3. Поиск по списку\n 4. Удалить запись\n 5. Изменить контакт\n 6. Выйти')

# Функция для вывода всех записей в справочнике
def show_phonebook(date):
    with open('contacts.txt', 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            print(row)