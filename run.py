#


from waitress import serve
from FunnyBag.main import FrameWork
import config
from views import routes
import logging
# Создаем объект WSGI-приложения
application = FrameWork(config, routes)

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

serve(application, listen='*:8080')

