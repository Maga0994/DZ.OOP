class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):  # Оцениваем Лекторов
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

# -------------------------------------------------------------------

    def _avarage_student_score(self):  # Подсчет среднего балла за домашку Студентов
        avg_2 = []
        for value in self.grades.values():
            avg_2.extend(value)
        res = sum(avg_2) / len(avg_2)
        return round(res, 2)

    def __str__(self):  # Перевод в магический метод
        lec = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self._avarage_student_score()}\nКурсы в процессе изучения: {", ". join(self.courses_in_progress)}\nЗавершенные курсы: {" ". join(self.finished_courses)}'
        return lec

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение не верно!')
            return
        return self._avarage_student_score() < other._avarage_student_score()
# -------------------------------------------------------------------
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def _avarage_lector_score(self):  # Подсчет среднего балла за лекции Лекторов
        avg = []
        for value in self.grades.values():
            avg.extend(value)
        res = sum(avg) / len(avg)
        return round(res, 2)

    def __str__(self):  # Перевод в магический метод
        lec = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за леции: {self._avarage_lector_score()}'
        return lec

# ----------------------------------------------------------------
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение не верно!')
            return
        return self._avarage_lector_score() < other._avarage_lector_score()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):  # Оцениваем Студентов
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):  # Перевод в магический метод
        lec = f'Имя: {self.name}\nФамилия: {self.surname}'
        return lec

# ------------------------------------------------------------------------------

# Создаем студентов
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

best_student_2 = Student('Nata', 'Tupina', 'famale')
best_student_2.courses_in_progress += ['Git']
best_student_2.finished_courses += ['Введение в программирование']

# ------------------------------------------------------------------------------

# Создаем Ревьюеров
master_review = Reviewer('Joe', 'Biden')
master_review.courses_attached += ['Python']
master_review.courses_attached += ['Git']

master_review_2 = Reviewer('Vladimir', 'Putin')
master_review_2.courses_attached += ['Python']
master_review_2.courses_attached += ['Git']

# Оценка студентов от Ревьюера
master_review.rate_hw(best_student, 'Python', 10)
master_review.rate_hw(best_student, 'Python', 10)
master_review.rate_hw(best_student, 'Python', 8)

master_review.rate_hw(best_student, 'Git', 10)
master_review.rate_hw(best_student, 'Git', 10)
master_review.rate_hw(best_student, 'Git', 9)

master_review_2.rate_hw(best_student_2, 'Git', 9)
master_review_2.rate_hw(best_student_2, 'Git', 10)
master_review_2.rate_hw(best_student_2, 'Git', 6)

# Имя Фамилия Ревьюера который оценивает Студентов
print('Ревьюеры:')
some_reviewer = master_review
some_reviewer_2 = master_review_2
print(some_reviewer, some_reviewer_2, sep='\n\n')
print()

# Средний балл студента по ДЗ
print('Студенты:')
some_student = best_student
some_student_2 = best_student_2
print(some_student, some_student_2, sep='\n\n')
print()
print(some_student < some_student_2)
print()

# ------------------------------------------------------------------------------
# Создаем Лекторов
best_lector = Lecturer('Aleksandr', 'Borodach')
best_lector.courses_attached += ['Python']

best_lector_2 = Lecturer('Roman', 'Abramovich')
best_lector_2.courses_attached += ['Git']

# Оценка лекторов от Студентов
best_student.rate_lector(best_lector, 'Python', 10)
best_student.rate_lector(best_lector, 'Python', 6)
best_student.rate_lector(best_lector, 'Python', 6)

best_student.rate_lector(best_lector_2, 'Git', 7)
best_student.rate_lector(best_lector_2, 'Git', 10)
best_student.rate_lector(best_lector_2, 'Git', 9)

best_student_2.rate_lector(best_lector_2, 'Git', 10)
best_student_2.rate_lector(best_lector_2, 'Git', 9)
best_student_2.rate_lector(best_lector_2, 'Git', 10)

# Выводим средний балл оценок Лекторов
print('Лекторы:')
some_lecturer = best_lector
some_lecturer_2 = best_lector_2
print(some_lecturer, some_lecturer_2, sep='\n\n')
print()
print(some_lecturer < some_lecturer_2)
print()

# ------------------------------------------------------------------------------

student_list = [best_student, best_student_2]

def student_avg_score_in_course(student_list, course):
    score_list = []
    for student in student_list:
        for value in student.grades.values():
            if isinstance(student, Student) and course in student.courses_in_progress and course in student.grades:
                score_list.extend(value)
    res = sum(score_list) / len(score_list)
    return round(res, 2)

print(f'Средняя оценка для всех студентов по курсу {"Python"}: {student_avg_score_in_course(student_list, "Python")}')
print(f'Средняя оценка для всех студентов по курсу {"Git"}: {student_avg_score_in_course(student_list, "Git")}')


lecturer_list = [best_lector, best_lector_2]

def lector_avg_score_in_course(lecturer_list, course):
    score_list_lect = []
    for lector in lecturer_list:
        for value in lector.grades.values():
            if isinstance(lector, Lecturer) and course in lector.courses_attached and course in lector.grades:
                score_list_lect.extend(value)
    res = sum(score_list_lect) / len(score_list_lect)
    return round(res, 2)

print(f'Средняя оценка для всех лекторов по курсу {"Python"}: {lector_avg_score_in_course(lecturer_list, "Python")}')
print(f'Средняя оценка для всех лекторов по курсу {"Git"}: {lector_avg_score_in_course(lecturer_list, "Git")}')
