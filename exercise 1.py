# Определение класса SchoolClass с атрибутами и методами для работы с классной группой
class SchoolClass:
    # Метод инициализации атрибутов класса
    def __init__(self, class_name, teacher, subjects, students):
        self.class_name = class_name  # Инициализация атрибута классной группы
        self.teacher = teacher  # Инициализация атрибута классного руководителя
        self.subjects = subjects  # Инициализация атрибута предметов
        self.students = students  # Инициализация атрибута студентов

    # Методы для чтения значений атрибутов
    def get_class_name(self):
        return self.class_name  # Возвращение значения атрибута классной группы

    def get_teacher(self):
        return self.teacher  # Возвращение значения атрибута классного руководителя

    def get_subjects(self):
        return self.subjects  # Возвращение значений атрибута предметов

    def get_students(self):
        return self.students  # Возвращение значений атрибута студентов

    # Методы для записи значений атрибутов
    def set_class_name(self, value):
        self.class_name = value  # Запись нового значения атрибута классной группы

    def set_teacher(self, value):
        self.teacher = value  # Запись нового значения атрибута классного руководителя

    def set_subjects(self, value):
        self.subjects = value  # Запись нового значения атрибута предметов

    def set_students(self, value):
        self.students = value  # Запись нового значения атрибута студентов

# Создание экземпляров класса
class1 = SchoolClass("10A", "Иванов И.И.", ["Математика", "Физика", "Информатика"], ["Петров П.П.", "Сидоров С.С.", "Соколов К.К."])
class2 = SchoolClass("5Б", "Сидорова М.М.", ["Русский язык", "История", "Литература"], ["Пупкин А.А.", "Кузнецов Д.Д.", "Лебедев В.В."])

# Показать значения свойств объектов
print(f"Класс: {class1.get_class_name()}, Учитель: {class1.get_teacher()}, Предметы: {class1.get_subjects()}, Студенты: {class1.get_students()}")
print(f"Класс: {class2.get_class_name()}, Учитель: {class2.get_teacher()}, Предметы: {class2.get_subjects()}, Студенты: {class2.get_students()}")