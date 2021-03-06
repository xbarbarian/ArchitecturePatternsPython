"""Модуль, содержащий контроллеры веб-приложения"""
from FunnyBag.templator import render
from FunnyBag.decorators import AppRoute

routes = {}


@AppRoute(routes=routes, url='/')
class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


@AppRoute(routes=routes, url='/about/')
class About:
    def __call__(self, request):
        return '200 OK', render('about.html')
