from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):

    def __init__(self, value):
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError('10 digits for phone')
        super().__init__(value)
    
    

class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phone.remove(phone)
                return True
        return False 
    
    def edit_phone(self, old_p_numb, new_p_numb):
        self.remove_phone(old_p_numb)
        self.add_phone(new_p_numb)

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone 
        return None
    
    def __str__(self):
        phone_strings = '; '.join(p.value for p in self.phones)
        return f"Имя контакта: {self.name.value}, Номер контакта: {phone_strings}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record
        print(f"Запись для контакта '{record.name.value}' добавлена")

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Запись для контакта '{name}' удалена.")
            return True
        print(f"Ошибка:Контакт '{name}' не найден.")
        return False


ab = AddressBook()

try:
    rec = Record("john Doe")
    rec.add_phone("322121")
except ValueError as e:
    print(f" Ошибка при добавлении телефона: {e}")


rec = Record("Vasya pupkin")
rec.add_phone("1122332211")
rec.add_phone("4443133334")
ab.add_record(rec)

found_record = ab.find("Vasya pup")
if found_record:
    print("\nНайдена запись")
    print(found_record)
