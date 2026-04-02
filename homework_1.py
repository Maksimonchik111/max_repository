class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        if self.higher_education:
            education= 'есть высшее образование'
        else:
            education  = "высшего образования нет"
        return f'меня зовут {self.name}, я родился в {self.birth_date} году, по профессии {self.occupation}, {education}'


person1 = Person("Максим", 2009, "программист", True)
person2 = Person("Олег", 1998, "уборщик", False)
print(f'Имя: {person1.name}, Дата рождения: {person1.birth_date}, Профессия: {person1.occupation}, Образование: {person1.higher_education}')
print(f'Имя: {person2.name}, Дата рождения: {person2.birth_date}, Профессия: {person2.occupation}, Образование: {person2.higher_education}')
print(person1.introduce())
print(person2.introduce())

