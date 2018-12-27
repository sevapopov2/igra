import os, pickle
from year import year
from student import Student

class level:
    tired_rate = 1

print('Добро пожаловать! Выберите пункт меню:')
print('Нажмите 1, чтобы начать новую игру')
print('Нажмите 2, чтобы продолжить ранее начатую игру')
print('Нажмите 4, чтобы выйти')
menu_item =0
submenu_item = 0
while menu_item != 4:
    os.system('cls')
    print('Нажмите 1, чтобы начать новую игру')
    print('Нажмите 2, чтобы продолжить ранее начатую игру')
    print('Нажмите 4, чтобы выйти')
    print('Сделайте ваш выбор')
    menu_item=int(input())
    if menu_item==1:
        print('Начинаем новую игру!')
        print('Напишите, как вас зовут?')
        stu_name =input()
        student =Student(stu_name)
        print('Вы', student.name)
        print('На данный момент вы учитесь в', student.student_study)
        student.student_preferences()
        print('Нажмите 1, чтобы пойти учиться')
        print('Нажмите 2, чтобы пойти порепетировать')
        print('Нажмите 3, чтобы отдохнуть')
        while student.action != 4:
            student.action = int(input())
            if student.action == 1:
                student.study_knolidge()
                student.student_preferences()
                if student.study_count >=5:
                    print('Вы так много трудитесь сегодня. Возможно, Вы немного устали. Отдохните немного!')
            if student.action == 2:
                student.study_rehers()
                print('Молодец!')
                student.student_preferences()
            if student.action == 3:
                student.take_rest()
                print('Вы немного отдохнули')
                student.student_preferences()
        output = open('data.pkl', 'wb')
        pickle.dump(student, output, 2)
        output.close()
        os.system('pause')
    if menu_item==2:
        print('Продолжаем!')
        input = open('data.pkl', 'rb')
        student = pickle.load(input)
        input.close()
        print(student.name)
        print('Ваш уровень', student.level)
        print('Ваша техника равна', student.technique)
        print('Ваш уровень успеваемости', student.success_level)
        print('На данный момент вы учитесь в', student.student_study)

        os.system('pause')