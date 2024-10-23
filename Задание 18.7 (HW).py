import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам.
        4. Вывод информации по всем оценкам для определенного ученика
        5. Вывести средний балл по всем предметам для определенного ученика
        6. Удаление предмета
        7. Добавление предмета
        8. Переименование предмета
        9. Добавление оценок
        10. Удаление оценок
        11. Изменение оценок
        12. Удалине ученика
        13. Добавление студента
        14. Выход из программы.
        ''')

while True:
    command = input('Введите команду: ')
    if command.isdigit():
        command = int(command)
    else:
        print('Ввод команды принимает только цифры!')
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Вывод информации по всем оценкам для определенного ученика: ')
        name_stud = input(f'{students}\nВведите имя ученика:\n ')
        if name_stud in students_marks.keys():
            for class_ in classes:
                print(f'\t{class_} - {students_marks[name_stud][class_]}')
        else:
            print('Данного ученика нет в списке!')
    elif command == 5:
        print('5. Вывести средний балл по всем предметам для определенного ученика')
        print(students)
        name_stud = input('Введите имя студента: ')
        if name_stud in students_marks.keys():
            print(f'Средний балл ученика {name_stud} по предметам: !')
            for class_ in classes:
                marks_sum = sum(students_marks[name_stud][class_])
                marks_count = len(students_marks[name_stud][class_])
                print(f'\t{class_} - {marks_sum // marks_count}')
        else:
            print('Данного ученика нет в списке!')
    elif command == 6:
        print('6. Удаление предмета')
        print(classes)
        name_clas = input('Введите название предмета:\n ')
        if name_clas in classes:
            classes.remove(name_clas)
            for student in students:
                del students_marks[student][name_clas]
            print(f'Предмет {name_clas} аннигилирован!')
        else:
            print('Данного предмета нет в списке!')
    elif command == 7:
        print('7. Добавление предмета!')
        print(classes)
        name_clas = input('Введите название предмета:\n ')
        classes.append(name_clas)
        for student in students:
            students_marks[student][name_clas] = []
    elif command == 8:
        print('8. Переименование предмета')
        print(classes)
        old_clas = input('Введите название предмета который хотите переименовать: \n')
        if old_clas in classes:
            new_clas = input('Введите новое название предмета: \n')
            for student in students:
                students_marks[student][new_clas] = students_marks[student][old_clas]
                del students_marks[student][old_clas]
            classes.remove(old_clas)
            classes.append(new_clas)
            print(f'Предмет {old_clas} переименован в {new_clas} ')
        else:
            print(f'Предмета {old_clas} не в списке!')
    elif command == 9:
        print('9. Добавление оценок')
        print(students)
        name_stud = input('Введите имя студента: ')
        if name_stud in students:
            print(classes)
            name_clas = input('Введите название предмета: ')
            if name_clas in classes:
                mark = input('Сколько оценок нужно добавить: ')
                if mark.isdigit():
                    mark = int(mark)
                    if mark == 1:
                        new_mark = int(input('Введите оценку: '))
                        students_marks[name_stud][name_clas].append(new_mark)
                    elif mark > 1:
                        for mar in range(mark):
                            mar = int(input(f'Введите оценку:'))
                            students_marks[name_stud][name_clas].append(mar)
                        print(f'Оценки ученика {name_stud} по предмету {name_clas} = {students_marks[name_stud][name_clas]}')
                else:
                    print('Кол-во оценок вводится цифрой!')
            else:
                print('Название предмета введено не верно!')
        else:
            print('Такого студента не существует!')
    elif command == 10:
        print('10. Удаление оценок')
        print(students)
        name_stud = input(f'Введите имя студента у которого хотите удалить оценки: ')
        if name_stud in students:
            print(classes)
            name_clas = input('Введите название предмета: ')
            if name_clas in classes:
                print(f'Студент - {name_stud}\nПредмет - {name_clas}\n {students_marks[name_stud][name_clas]}')
                mark = int(input('Введите индекс оценки которую хотите удалить: '))
                students_marks[name_stud][name_clas].pop(mark)
                print(students_marks[name_stud][name_clas])
            else:
                print('Нет такого предмета!')
        else:
            print('Нет такого студента!')
    elif command == 11:
        print('11. Изменение оценок')
        print(students)
        name_stud = input(f'Введите имя студента у которого хотите изменить оценку: ')
        if name_stud in students:
            print(classes)
            name_clas = input('Введите название предмета: ')
            if name_clas in classes:
                print(f'Студент - {name_stud}\nПредмет - {name_clas}\n {students_marks[name_stud][name_clas]}')
                mark = int(input('Введите номер оценки которую хотите изменить: '))
                students_marks[name_stud][name_clas].pop(mark-1)
                add_mark = int(input('Введите новую оценку: '))
                students_marks[name_stud][name_clas].insert(mark-1, add_mark)
                print(students_marks[name_stud][name_clas])
            else:
                print('Нет такого предмета!')
        else:
            print('Нет такого студента!')

    elif command == 12:
        print('12. Удалине ученика')
        print(students)
        name_stud = input('Введите имя студента которого хотите удалить: ')
        if name_stud in students:
            students.remove(name_stud)
            print(students)
        else:
           print('Нет такого студента!')
    elif command == 13:
        print('13. Добавление студента')
        print(students)
        name_stud = input('Введите имя студента которого хотите добавить: ')
        if not name_stud in students:
            students.append(name_stud)
            students_marks[name_stud] = {}
            for clas in classes:
                students_marks[name_stud][clas] = []
        else:
            print('Такоей студент уже есть!')
        print(students)

    elif command == 14:
        break
