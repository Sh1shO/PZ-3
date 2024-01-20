class SchoolClass:
    # Определяем класс SchoolClass со свойствами и методами
    def __init__(self, teacher, subjects, students):
        # Проверяем, соответствуют ли условиям ограничениям и создаем объект
        if not isinstance(teacher, str) or len(teacher) > 100:
            raise ValueError("Количество символов в имени руководителя не должно превышать 100 символов.")
        if not isinstance(subjects, list) or not all(isinstance(subject, str) for subject in subjects):
            raise ValueError("Темы должны быть представлены массивом.")
        if not isinstance(students, list) or not all(isinstance(student, str) for student in students):
            raise ValueError("Учащиеся должны быть представлены массивом.")
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
        return f"Учитель: {self.teacher}\nПредметы: {', '.join(self.subjects)}\nСтуденты: {', '.join(self.students)}"


if __name__ == "__main__":
    # Создаем два экземпляра класса SchoolClass
    class1 = SchoolClass("Иванов Иван", ["Математика", "Физика", "Информатика"], ["Петров Пётр", "Сидоров Сергей", "Соколов Клим"])
    class2 = SchoolClass("Сидорова Мария", ["Русский язык", "История", "Литература"], ["Пупкин Антон", "Кузнецов Денис", "Лебедев Виктор"])
    class1.sort_subjects()
    class2.sort_subjects()
    class1.sort_students()
    class2.sort_students()

    # Выводим значения свойств объектов с помощью метода __str__
    print(class1)
    print()
    print(class2)