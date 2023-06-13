# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

# Функция для чтения данных из файла справочника
def read_contacts(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        # Создаем словарь, в котором будем хранить данные о контактах
        contacts = {}
        for line in lines:
            name, phone_number = line.strip().split(',')
            contacts[name] = phone_number
        return contacts

# Функция для записи данных в файл справочника
def write_contacts(filename, contacts):
    with open(filename, 'w') as f:
        for name, phone_number in contacts.items():
            f.write(f"{name},{phone_number}\n")

# Функция для добавления нового контакта в справочник
def add_contact(filename, name, phone_number):
    contacts = read_contacts(filename)
    contacts[name] = phone_number
    write_contacts(filename, contacts)
    print(f"Контакт {name} успешно добавлен в справочник")

# Функция для изменения данных о существующем контакте
def update_contact(filename, name):
    contacts = read_contacts(filename)
    if name in contacts:
        new_phone_number = input("Введите новый номер телефона для контакта: ")
        contacts[name] = new_phone_number
        write_contacts(filename, contacts)
        print(f"Данные о контакте {name} успешно изменены")
    else:
        print(f"Контакт {name} не найден в справочнике")

# Функция для удаления контакта из справочника
def delete_contact(filename, name):
    contacts = read_contacts(filename)
    if name in contacts:
        del contacts[name]
        write_contacts(filename, contacts)
        print(f"Контакт {name} успешно удален из справочника")
    else:
        print(f"Контакт {name} не найден в справочнике")

filename = "contacts.txt"
add_contact(filename, "Иван Иванов", "123-45-67")
add_contact(filename, "Петр Петров", "987-65-43")

update_contact(filename, "Иван Иванов")
delete_contact(filename, "Петр Петров")