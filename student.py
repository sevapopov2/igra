from year import year
from events import randomevent
class Student:
    name=''
    level=1
    technique = 0
    success_level = 0
    health_level=100
    money_count=0
    study_count =0
    knolidge_level = 0
#Уровень знаний. Он будет измеряться в процентах. Процент знаний - это прогресс знаний до следующего уровня.
    rehers_count=0
#rehers count это количество репитиций. От репитиций техника повышается.
    rest_count =0
    tired_level = 0
    studyyear = year()
#Уровень усталости измеряется в процентах от 0 до 100.
    student_study ='Музыкальная школа'
    action = 0

    def __init__(self, name):
        self.name=name

    def student_preferences(self):
        print('Ваш уровень', self.level)
        print('Ваш уровень знаний', self.knolidge_level)
        print('Ваша техника ', self.technique)
        print('Вы устали на', self.tired_level, 'процентов')

    def set_technique_level(self, technique):
        self.technique = self.technique + technique
        if self.technique >= 100:
            self.technique = 100

    def set_tired_level(self, tired_level):
        self.tired_level = self.tired_level + tired_level
        if self.tired_level >= 100:
            self.tired_level = 100

    def set_knolidge_level(self, knolidge_level):
        self.knolidge_level = self.knolidge_level + knolidge_level
        if self.knolidge_level > 100:
            self.knolidge_level = 100
#        if self.studyyear.holidays == 1:
#            self.knolidge_level = self.knolidge_level
#            print('У вас каникулы. Вы не можете учиться.')

    def study_rehers(self):
        if studyyear.ib:
            print('У вас же инструмент сломался! Вы не можете репитировать!')
        else:
            self.rehers_count = self.rehers_count + 1
            if self.tired_level == 0:
                self.set_technique_level(10)
                self.set_tired_level(5)
            elif self.tired_level == 100:
                self.set_technique_level(-1)
            else:
                self.set_technique_level(10 * (100 - self.tired_level) / 100)
            self.studyyear.daychange()
#        self.studyyear.quarterending()

    def study_knolidge(self):
        if self.studyyear.holidays == 0:
            self.study_count = self.study_count + 1
            self.set_tired_level(5)
            if self.tired_level == 0:
                self.set_knolidge_level(10)
            elif self.tired_level == 100:
                self.set_knolidge_level(-1)
            else:
                self.set_knolidge_level(10 * (100 - self.tired_level) / 100)
            self.studyyear.daychange()

    def take_rest(self):
        self.rest_count = self.rest_count + 1
        if self.tired_level >= 10:
            self.tired_level = self.tired_level - 10
        else:
            self.tired_level=0
        self.studyyear.daychange()
#        self.studyyear.quarterending()
