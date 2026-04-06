from datetime import datetime
class Person:
    def __init__(self, name, birth_date, occupation,higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.today()

        age = today.year - birth.year

        return f'Возраст: {age}'

    @property
    def introduce(self):
        if self.__higher_education:
            education= 'есть высшее образование'
        else:
            education  = "высшего образования нет"

        return f'Привет, меня зовут {self.name}, я родился  {self.__birth_date}, по профессии {self.__occupation}, {education}'


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name, higher_education):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    @property
    def introduce(self):
        if self._Person__higher_education:
            education= 'есть высшее образование'
        else:
            education  = "высшего образования нет"

        return f'Привет, меня зовут {self.name}, я родился  {self._Person__birth_date}, по профессии {self._Person__occupation}, я учился с Максимом в {self.group_name} , {education} '


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby, higher_education):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    @property
    def introduce(self):
        if self._Person__higher_education:
            education= 'есть высшее образование'
        else:
            education  = "высшего образования нет"

        return f'Привет, меня зовут {self.name}, я родился  {self._Person__birth_date}, по профессии {self._Person__occupation}, мое хобби {self.hobby}, {education}'



class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, hobby, shared_memory, higher_education):
        super().__init__(name, birth_date, occupation, hobby,higher_education)
        self.shared_memory = shared_memory

    @property
    def introduce(self):
        return f"{super().introduce}, наше общее воспоминание: {self.shared_memory}"


classmate1 = Classmate("Амир", "27.10.2009", "программист", "10G", False)
classmate2 = Classmate("Тимур", "22.01.2011", "строитель", "8E", False)
friend1 = Friend("Илья", "22.11.2009", "курьер", "шить носки", True)
friend2 = Friend("Омурбек", "11.10.2009", "официант", "смотреть фильмы", False)

people = [Person('Евлампий', "12.11.1999", "геодезист", True), classmate1, classmate2, friend1, friend2]
for p in people:
    print(p.introduce)

best_friend = BestFriend("Артур", "23.12.2009", "программист", "видеоигры", "кушали кириешки", False)
print(best_friend.introduce)

print(classmate2.age)
print(best_friend.age)