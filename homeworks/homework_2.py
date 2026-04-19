class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        return f'меня зовут {self.name}, я родился  {self.birth_date}, по профессии {self.occupation}'


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        return f'меня зовут {self.name},я одноклассник Максима, я родился  {self.birth_date}, по профессии {self.occupation}, учусь в {self.group_name} '


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    def introduce(self):
        return f'меня зовут {self.name},я друг Максима, я родился  {self.birth_date}, по профессии {self.occupation}, мое хобби {self.hobby}'


class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        return f"{super().introduce()}, наше общее воспоминание {self.shared_memory}"


classmate1 = Classmate("Амир", "27.10.2009", "программист", "10G")
classmate2 = Classmate("Тимур", "22.01.2011", "строитель", "8E")
friend1 = Friend("Илья", "22.11.2009", "курьер", "шить носки")
friend2 = Friend("Омурбек", "11.10.2009", "официант", "смотреть фильмы")

people = [Person('Евлампий', "12.11.1999", "геодезист"), classmate1, classmate2, friend1, friend2]
for p in people:
    print(p.introduce())

best_friend = BestFriend("Артур", "23.12.2009", "программист", "видеоигры", "кушали кириешки")
print(best_friend.introduce())
