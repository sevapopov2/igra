from events import randomevent
import random
class year:
    currentyear = 1
    day = 1
    week = 1
    weekspast = 0
    weeksleft = 0
    weekscount = 3
    breakdayscount = 0
    ibmoneycount = 0
#Число денег, выдаваемое студенту, когда инструмент ломается

    ibmoneyneeded = 0
#Число денег, необходимое на починку инструмента
    holidaysweek = 1
    quarter = 1
    holidays = 0
    learningday = 0

    def yearchange(self):
        self.currentyear = self.currentyear + 1
        self.week = 1
        self.weekscount = 3

    def quarterending(self):
        self.quarter = self.quarter + 1
        self.weekscount = self.weekscount + 2
        if self.quarter > 4:
            self.quarter = 1

    def holidaysstart(self):
        self.holidays = 1

    def holidaysend(self):
        self.holidays = 0
        self.quarterending()

    def weekchange(self):
        self.day = 1
        self.weeksleft = self.weekscount - self.week
        self.week = self.week + 1
        print('Остаток от деления ', self.week % 3)
        if self.week % 3 == 0:
            self.holidaysstart()
        if self.week % 3 == 1:
            self.holidaysend()
        if self.week > 12:
            self.yearchange()
    
    def daychange(self):
        self.day = self.day + 1
        if self.breakdayscount == 0:
            ib = randomevent.instrumentbreak()
            if (ib):
                print('Инструмент сломался: ', ib)
                self.breakdayscount = random.randint(1, 7)
                self.ibmoneycount = random.randint(0, 100)
                print('Поскольку ваш инструмент сломался, мы дадим вам возможность его починить. Вам выдали', self.ibmoneycount, 'рублей для этого')
                self.ibmoneyneeded = random.randint(1, 100)
                print('За починку вашего инструмента необходимо заплатить', self.ibmoneyneeded, 'рублей')

        if self.breakdayscount > 0:
            if self.ibmoneycount >= self.ibmoneyneeded:
                self.ibmoneycount = self.ibmoneycount - self.ibmoneyneeded
                self.breakdayscount = 0
                print('Вы заплатили', self.ibmoneycount, 'рублей. Теперь ваш инструмент в порядке')
                if self.ibmoneycount < self.ibmoneyneeded:
                self.breakdayscount = self.breakdayscount - 1
                print('Ваш инструмент починится через',self.breakdayscount, 'дней')
            
        print('Тип недели ', self.holidays)
        if self.day > 7:
            self.weekchange()
            print('Год', self.currentyear)
            print('Четверть ', self.quarter)
            print('Неделя ', self.week)
            print('Тип недели ', self.holidays)
            print('До каникул осталось ', self.weeksleft, ' недель')
        print('День ', self.day)

    def learningday(self):
        if self.holidays == 1:
            self.learningday = 0
        if self.learningday == 0:
            self.holidays = 1
