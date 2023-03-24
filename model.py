import os
import re

def read_phonebook():
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        pass

    return None

# Функция для добавления записи
def add_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    with open('contacts.txt', "a") as f:
        f.write(f"{last_name} {first_name} {middle_name} {phone_number}\n")
    
    print("Контакт успешно добавлен\n")

# Функция поиска
def search_contacts():
    search_string = input("Введите строку для поиска: ")
    results = []
    with open('contacts.txt', 'r') as f:
        for line in f:
            if search_string in line:
                results.append(line.strip())
    if results:
        print(f"Результаты поиска для '{search_string}\n':")
        for result in results:
            print(result)
    else:
        print(f"Ничего не найдено для '{search_string}\n'")
        

# Функция для удаления контакта
def delete_contact():
    name = input("Введите имя, фамилию или отчество контакта, который нужно удалить: ")
    with open('contacts.txt', 'r') as f:
        lines = f.readlines()
    with open('contacts.txt', 'w') as f:
        for line in lines:
            if name not in line:
                f.write(line)
    print("Контакт успешно удален\n")

# Функция для изменения записи
def edit_contact():
    name = input('Введите данные для поиска: ')

    with open('contacts.txt', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].startswith(name):
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            new_line = f"{last_name} {first_name} {middle_name} {phone_number}\n"
            lines[i] = new_line

            with open('contacts.txt', 'w') as f:
                f.writelines(lines)
            print(f"Запись с именем '{name}'")
            return

    print('Запись не найдена!')