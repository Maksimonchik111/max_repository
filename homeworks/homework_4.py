class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return len(phone_number) == 10


class ContactList:
    all_contacts = []
    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError("Номер должен состоять только из 10 символов!")



class Library:
    def __init__(self, city, books=None):
        self.city = city
        self.books = books

    def __str__(self):
        return f'<Library object, city: {self.city},books: {len(self.books)}>'

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        print(f'Ищем книгу: {item}')
        return item in self.books

    def __bool__(self):
        return len(self.books) > 5







lib = Library("Бишкек", books=["Война и мир", "1984", "Мастер и Маргарита"])
print(lib)

print("1984" in lib)
print("Гарри Поттер" in lib)
if lib:
    print("Библиотека большая (более 5 книг)")
else:
    print("Библиотека маленькая")

lib2 = Library("Москва", books=["Всадник без головы", "Гарри Поттер", "Последнее желание", "Метро 2033", "Мертвые души", "Идиот"])
print(lib2)

print("Последнее желание" in lib2)
if lib2:
    print("Библиотека большая (более 5 книг)")
else:
    print("Библиотека маленькая")
