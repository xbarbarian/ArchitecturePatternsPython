import quopri

# Класс-Абстрактный пользователь
from .notification import ConsoleWriter, FileWriter, Subject


class User:
    auto_id = 0

    def __init__(self, dict_data):
        self.first_name = dict_data['first_name']
        self.last_name = dict_data['last_name']
        self.age = dict_data['age']
        self.id = User.auto_id
        self.observers = []
        self.course = dict_data['course']
        self.email = dict_data['email']
        User.auto_id += 1


# Класс-Преподаватель
class Teacher(User):
    pass


# Класс-Студент
class Student(User, Subject):

    def __init__(self, dict_data):
        super().__init__(dict_data)
        self.phone = dict_data['phone']

        # super().__init__()

    def add_student(self, site):
        self.notify_student(site)


# Класс-Фабрика пользователей
class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_, dict_data):
        return cls.types[type_](dict_data)


# Класс-Курс
class Course:
    auto_id = 0

    def __init__(self, name, course_type):
        self.name = name
        self.type = course_type
        self.id = Course.auto_id
        Course.auto_id += 1


# Класс-Тип курсов курсов
class CourseType:
    auto_id = 0

    def __init__(self, param):
        self.name = param
        self.id = CourseType.auto_id
        CourseType.auto_id += 1


# Класс-Интерактивный курс
class InteractiveCourse(Course):
    pass


# Класс-Курс в записи
class RecordCourse(Course):
    pass


# Класс-Фабрика курсов
class CourseFactory:
    types = {
        'interactive': InteractiveCourse,
        'record': RecordCourse
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


# Класс-Категория
class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []
        self.teachers = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


# Класс-Основной интерфейс проекта
class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []
        self.type_courses = []

    # Type course
    @staticmethod
    def type_course(param):
        return CourseType(param)

    def type_course_delete(self, id):
        for item in self.type_courses:
            if item.id == id:
                self.type_courses.pop(id)
                return self.type_courses
        raise Exception(f'Нет типа курса с id = {id}')

    def type_course_detail(self, id):
        for item in self.type_courses:
            if item.id == id:
                return item
        raise Exception(f'Нет типа курса с id = {id}')

    def type_course_update(self, id, name):
        for item in self.type_courses:
            if item.id == id:
                item.name = name
                return self.type_courses
        raise Exception(f'Нет типа курса с id = {id}')

    def find_type_course_by_id(self, id):
        for item in self.type_courses:
            if item.id == id:
                return item
        raise Exception(f'Нет типа курса с id = {id}')

    # Course
    def create_course(self, name, type_):
        return Course(name, type_)

    def delete_course(self, id):
        for item in self.courses:
            if item.id == id:
                self.courses.pop(id)
                return self.courses
        raise Exception(f'Нет типа курса с id = {id}')

    def find_course_by_id(self, id):
        for item in self.courses:
            if item.id == id:
                return item
        raise Exception(f'Нет типа курса с id = {id}')

    @staticmethod
    def create_user(type_, dict_data):
        return UserFactory.create(type_, dict_data)

    def delete_student(self, id):
        for item in self.students:
            if item.id == id:
                self.students.pop(id)
                return self.students
        raise Exception(f'Нет типа курса с id = {id}')

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            # print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с id = {id}')

    # @staticmethod
    # def create_course(type_, name, category):
    #     return CourseFactory.create(type_, name, category)

    @staticmethod
    def create_course_with_type(type_, name, category):
        return CourseFactory.create(type_, name, category)

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        if type(val) == str:
            val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val_b)
            return val_decode_str.decode('UTF-8')
        else:
            return list(map(int, val))


# порождающий паттерн Синглтон
class SingletonByName(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=SingletonByName):

    def __init__(self, name, writer=ConsoleWriter(), writer_file=FileWriter("logs.txt")):
        self.name = name
        self.writer = writer
        self.writer_file = writer_file

    def log(self, text):
        # text = f'log---> {text}'
        self.writer.write(text)
        self.writer_file.write(text)
