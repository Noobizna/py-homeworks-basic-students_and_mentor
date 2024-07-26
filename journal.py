class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

  def av_sc(self):
      length = sum(map(len, self.grades.values()))
      sum_grades = sum(map(sum, self.grades.values()))
      if length == 0:
          print('У студента нет оценок')
      else:
          return round(sum_grades / length, 1)

  def validate_average_score(self, other):
      is_valid = self.av_sc() and other.av_sc() and isinstance(other, Student)
      if not is_valid:
          print('Не соответствует требованиям')
      return is_valid

  def __str__(self):
      res = (f'Имя: {self.name} \nФамилия: {self.surname} \n'
          f'Средняя оценка за домашние задания: {self.av_sc()} \n'
          f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
          f'Завершенные курсы: {", ".join(self.finished_courses)}')
      return res

  def __lt__(self, other):
      if self.validate_average_score(other):
          return self.av_sc() < other.av_sc()

  def __gt__(self, other):
      if self.validate_average_score(other):
          return self.av_sc() > other.av_sc()

  def __eq__(self, other):
      if self.validate_average_score(other):
          return self.av_sc() == other.av_sc()

  def __ne__(self, other):
      if self.validate_average_score(other):
          return self.av_sc() != other.av_sc()

  def rate_hw(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
          if course in lecturer.grades:
              lecturer.grades[course] += [grade]
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'


class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

class Lecturer(Mentor):
  def __init__(self):
      self.grades = {}
      self.courses_attached = []

  def __str__(self):
      res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.av_sc()}'
      return res

  def av_sc(self):
      length = sum(map(len, self.grades.values()))
      sum_grades = sum(map(sum, self.grades.values()))
      if length == 0:
          print('У лектора нет оценок')
      else:
          return round(sum_grades / length, 1)

  def validate_average_score(self, other):
      is_valid = self.av_sc() and other.av_sc() and isinstance(other, Lecturer)
      if not is_valid:
          print('Не соответствует требованиям')
      return is_valid

  def __lt__(self, other):
      if self.validate_average_score(other):
          return self.av_sc() < other.av_sc()

  def __gt__(self, other):
      if self.validate_average_score(other):
          return self.av_sc() > other.av_sc()

  def __eq__(self, other):
      if self.validate_average_score(other):
          return self.av_sc() == other.av_sc()

  def __ne__(self, other):
      if self.validate_average_score(other):
          return self.av_sc() != other.av_sc()

class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

  def __str__(self):
      return f'Имя: {self.name} \n Фамилия: {self.surname}'


# первый студент
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# ментор
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

#print(best_student.grades)

best_lecturer_1 = Lecturer()
best_lecturer_1.name = 'Ivan'
best_lecturer_1.surname = 'Ivanov'
best_lecturer_1.courses_attached = ['Python']

best_lecturer_2 = Lecturer()
best_lecturer_2.name = 'Petr'
best_lecturer_2.surname = 'Petrov'
best_lecturer_2.courses_attached += ['Java', 'Python']

cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Ostap', 'Bender')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

student_1 = Student('Denis', 'Sviridov', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Roman', 'Malikov', 'male')
student_2.courses_in_progress += ['Java', 'Python']
student_2.finished_courses += ['Введение в программирование']

student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_2.rate_hw(best_lecturer_2, 'Python', 10)
student_2.rate_hw(best_lecturer_2, 'Python', 8)
student_2.rate_hw(best_lecturer_2, 'Python', 9)

cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 10)

cool_reviewer_2.rate_hw(student_2, 'Java', 8)
cool_reviewer_2.rate_hw(student_2, 'Java', 7)
cool_reviewer_2.rate_hw(student_2, 'Java', 9)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}')
print()
print()

print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}')
print()
print()

student_list = [student_1, student_2]

lecturer_list = [best_lecturer_1, best_lecturer_2]



# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_student_grades(students, course):
  total_grades = 0
  total_count = 0

  for student in students:
      if course in student.grades:
          total_grades += sum(student.grades[course])
          total_count += len(student.grades[course])

  if total_count == 0:
      return 'Нет оценок'

  return round(total_grades / total_count, 1)

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecturer_grades(lecturers, course):
  total_grades = 0
  total_count = 0

  for lecturer in lecturers:
      if course in lecturer.grades:
          total_grades += sum(lecturer.grades[course])
          total_count += len(lecturer.grades[course])

  if total_count == 0:
      return 'Нет оценок'

  return round(total_grades / total_count, 1)

# Сравнение студентов
print(f'Результат сравнения студентов (по средним оценкам за домашние задания): '
    f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 < student_2}')

# Сравнение лекторов
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
    f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 < best_lecturer_2}')
print()

# Подсчет средней оценки за домашние задания по студентам
print(f'Средняя оценка за домашние задания по курсу Python: {average_student_grades(student_list, "Python")}')

# Подсчет средней оценки за лекции по лекторам
print(f'Средняя оценка за лекции по курсу Python: {average_lecturer_grades(lecturer_list, "Python")}')