#


from waitress import serve
from FunnyBag.main import Framework
import config
from views import routes
import logging

# Создаем объект WSGI-приложения
application = Framework(config, routes)

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

serve(application, listen='127.0.0.1:8080')

