class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if 10 >= grade >= 0:
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            if isinstance(lecturer,
                          Student) and course in self.courses_attached and course in lecturer.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += ['Поставил не правильную оценку']
                else:
                    lecturer.grades[course] = ['Поставил не правильную оценку']
            else:
                return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.sred()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')

    def sred(self):
        max_grades = 0
        summ = 0
        for course in self.grades:
            for grade in self.grades.get(course):
                max_grades += 1
                summ += grade
        if max_grades == 0:
            return 0
        return summ / max_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if 10 >= grade >= 0:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            if isinstance(student,
                          Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += ['Поставил не правильную оценку']
                else:
                    student.grades[course] = ['Поставил не правильную оценку']
            else:
                return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.sred()}\n')

    def sred(self):
        max_grades = 0
        summ = 0
        for course in self.grades:
            for grade in self.grades.get(course):
                max_grades += 1
                summ += grade
        if max_grades == 0:
            return 0
        return summ / max_grades


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


list_of_students = []
list_of_reviewers = []
list_of_lecturers = []

# Добавляю несколько студентов проверящих и лекторов
list_of_students.append(Student('Иван', 'Иванов', 'Мужчина'))
list_of_students.append(Student('Евгения', 'Манжалова', 'Женщина'))

list_of_reviewers.append(Reviewer('Антон', 'Бык'))
list_of_reviewers.append(Reviewer('Рома', 'Рык'))

list_of_lecturers.append(Lecturer('Руслан', 'Ахметов'))
list_of_lecturers.append(Lecturer('Андрей', 'Мавзолеев'))

# Добавляю курсы
list_of_students[0].courses_in_progress += ['Python']
list_of_students[0].courses_in_progress += ['Java']
list_of_students[0].courses_in_progress += ['SQL']
list_of_students[0].courses_in_progress += ['c++']
list_of_students[1].courses_in_progress += ['Python']
list_of_students[1].courses_in_progress += ['Java']
list_of_students[1].courses_in_progress += ['SQL']
list_of_students[1].courses_in_progress += ['c++']

list_of_reviewers[0].courses_attached += ['Python']
list_of_reviewers[0].courses_attached += ['Java']
list_of_reviewers[1].courses_attached += ['SQL']
list_of_reviewers[1].courses_attached += ['c++']

list_of_lecturers[0].courses_attached += ['Python']
list_of_lecturers[0].courses_attached += ['Java']
list_of_lecturers[1].courses_attached += ['SQL']
list_of_lecturers[1].courses_attached += ['c++']

# Ставлю оценки правильные
list_of_reviewers[0].rate_hw(list_of_students[0], 'Python', 9)
list_of_reviewers[0].rate_hw(list_of_students[1], 'Python', 7)
list_of_reviewers[0].rate_hw(list_of_students[0], 'Java', 6)
list_of_reviewers[0].rate_hw(list_of_students[1], 'Java', 4)
list_of_reviewers[0].rate_hw(list_of_students[0], 'SQL', 9)
list_of_reviewers[0].rate_hw(list_of_students[1], 'SQL', 7)
list_of_reviewers[0].rate_hw(list_of_students[0], 'c++', 2)
list_of_reviewers[0].rate_hw(list_of_students[1], 'c++', 2)

list_of_reviewers[1].rate_hw(list_of_students[0], 'Python', 4)
list_of_reviewers[1].rate_hw(list_of_students[1], 'Python', 8)
list_of_reviewers[1].rate_hw(list_of_students[0], 'Java', 7)
list_of_reviewers[1].rate_hw(list_of_students[1], 'Java', 5)
list_of_reviewers[1].rate_hw(list_of_students[0], 'SQL', 8)
list_of_reviewers[1].rate_hw(list_of_students[1], 'SQL', 6)
list_of_reviewers[1].rate_hw(list_of_students[0], 'c++', 3)
list_of_reviewers[1].rate_hw(list_of_students[1], 'c++', 4)

list_of_students[0].rate_hw(list_of_lecturers[0], 'Python', 8)
list_of_students[0].rate_hw(list_of_lecturers[0], 'Java', 6)
list_of_students[0].rate_hw(list_of_lecturers[1], 'SQL', 5)
list_of_students[0].rate_hw(list_of_lecturers[1], 'c++', 3)

list_of_students[1].rate_hw(list_of_lecturers[0], 'Python', 4)
list_of_students[1].rate_hw(list_of_lecturers[0], 'Java', 5)
list_of_students[1].rate_hw(list_of_lecturers[1], 'SQL', 8)
list_of_students[1].rate_hw(list_of_lecturers[1], 'c++', 10)


print('---------------\nСтуденты:\n')
for student in list_of_students:
    print(student)

print('---------------\nПроверяющие:\n')
for reviewer in list_of_reviewers:
    print(reviewer)

print('---------------\nЛекторы:\n')
for lecturer in list_of_lecturers:
    print(lecturer)


print('---------------\nСписок лекторов по убыванию по средней оценки за лекции:\n')


def get_sred_grade(element):
    return element.sred()


list_of_lecturers.sort(key=get_sred_grade, reverse=True)

for i in list_of_lecturers:
    print(i)


print('---------------\nСписок студентов по убыванию по средней оценки за дз:\n')


list_of_students.sort(key=get_sred_grade, reverse=True)

for i in list_of_students:
    print(i)
_=input()