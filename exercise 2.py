class SchoolClass:
    # Определяем класс SchoolClass со свойствами и методами
    def __init__(self, teacher, subjects, students):
        # Проверяем, соответствуют ли условиям ограничениям и создаем объект
        if not isinstance(teacher, str) or len(teacher) > 100:
            raise ValueError("Teacher name must be a string with a maximum of 100 characters.")
        if not isinstance(subjects, list) or not all(isinstance(subject, str) for subject in subjects):
            raise ValueError("Subjects must be a list of strings.")
        if not isinstance(students, list) or not all(isinstance(student, str) for student in students):
            raise ValueError("Students must be a list of strings.")
        self.teacher = teacher  # Задаем имя учителя
        self.subjects = list(set(subjects))  # Создаем список уникальных предметов
        self.students = list(set(students))  # Создаем список уникальных студентов

    def sort_subjects(self):
        # Метод для сортировки списка предметов по алфавиту
        self.subjects.sort()

    def sort_students(self):
        # Метод для сортировки списка студентов по алфавиту
        self.students.sort()

    def __str__(self):
        # Метод для вывода значений свойств объекта в читаемом формате
        return f"Teacher: {self.teacher}\nSubjects: {', '.join(self.subjects)}\nStudents: {', '.join(self.students)}"


if __name__ == "__main__":
    # Создаем два экземпляра класса SchoolClass
    class1 = SchoolClass("Иванов Иван", ["Математика", "Физика", "Химия", "Биология"], ["Петров Пётр", "Сидоров Иван", "Кузнецов Иван"])
    class2 = SchoolClass("Сидорова Светлана", ["Литература", "Информатика", "История"], ["Петрова Мария", "Кузнецова Анастасия", "Сидорова Софья"])
    class1.sort_subjects()
    class2.sort_subjects()
    class1.sort_students()
    class2.sort_students()

    # Выводим значения свойств объектов с помощью метода __str__
    print(class1)
    print()
    print(class2)