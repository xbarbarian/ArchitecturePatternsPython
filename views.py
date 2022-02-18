"""Модуль, содержащий контроллеры веб-приложения"""
from FunnyBag.templator import render
from FunnyBag.decorators import AppRoute


routes = {}


@AppRoute(routes=routes, url='/')
class Index:
    def __call__(self, request):
        return '200 OK', render('base.html')


@AppRoute(routes=routes, url='/about/')
class About:
    def __call__(self, request):
        return '200 OK', render('about.html')


#LIST

# Класс-контроллер - Страница "Список категорий"
@AppRoute(routes=routes, url='/category-list/')
class CategoryList:

    def __call__(self, request):
        logger.log('Получаем список категорий "В РАЗРАБОТКЕ"')
        return '200 OK', render('category.html',
                                objects_list=site.categories)

# Класс-контроллер - Страница "Список учителей"
@AppRoute(routes=routes, url='/teacher-list/')
class TeachersList:

    def __call__(self, request):
        logger.log('Получаем список учителей')
        return '200 OK', render('teachers.html',
                                objects_list=site.teachers)
