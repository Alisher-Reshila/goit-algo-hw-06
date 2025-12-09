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
        return phone 

    def remove_phone(self, phone_number):
        phone_obj = self.find_phone(phone_number)
        if phone_obj:
            self.phone.remove(phone_obj)
            return True
        raise ValueError(f"Телефонный номер {phone_number} не найден.")


    def edit_phone(self, old_p_numb, new_p_numb):
        new_phone_obj = self.add_phone(new_p_numb)
        old_phone_obj = self.find_phone(old_p_numb)
        if old_phone_obj:
            self.phones.remove(old_phone_obj)
            return new_phone_obj
        else:
            self.phones.remove(new_phone_obj)
            raise ValueError(f"Старый номер телефона {old_p_numb} не найден для замены.")
  

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
        return record 
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            deleted_record = self.data.pop(name)
            return deleted_record
        return None

ab = AddressBook()

try:
    rec = Record('Mars')
    rec.add_phone('1234567890')
    ab.add_record(rec)
    print(f"Добавлена запись: {ab.find('Mars')}")

    ab.find('Mars').edit_phone('1234567890','1234554321')
    print(f"Добавлена запись: {ab.find('Mars')}")

    ab.find('Mars').edit_phone('1234567888', '1233444554')

except ValueError as e:
    print(f"Перехвачена ошибка: {e}")
