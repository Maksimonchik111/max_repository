class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"{self.live()} {self.superpower()}"

class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"{self.live()} {self.viral()} {self.superpower()}"


class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return f"{self.earn()} и при этом {self.viral()}"



gs = GlowStreamer()
print(GlowStreamer.__mro__)
print(gs.live()) # Сработал метод класса Streamer потому что мы первым делом наследуемся от него и из за этого он первый в цепочке mro
vc = ViralCyborg()
print(ViralCyborg.__mro__)
print(vc.live()) # Сработал метод класса TikToker потому что мы первым делом наследуемся от него и из за этого он первый в цепочке mro
dm = DonateMage()
print(DonateMage.__mro__)
print(dm.live()) # Сработал метод класса Streamer потому что мы первым делом наследуемся от него и из за этого он первый в цепочке mroo