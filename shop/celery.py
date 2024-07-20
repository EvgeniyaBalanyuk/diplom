import os
from celery import Celery

# Задать стандартный модуль настроек Django для программы Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')  # Задается переменная 'DJANGO_SETTINGS_MODULE' для встроенной в Celery программы командной строки
app = Celery('shop')  # Создается экземпляр приложения
app.config_from_object('django.conf:settings', namespace='CELERY') # Используя метод "config_from_object" загружается любая кокретно-прикладная конфигурация из настроек проекта, namespace='CELERY' - все настройки проекта должны включать в свое имя префикс 'CELERY_'
app.autodiscover_tasks()  # Очередь заданий Celery будет автоматически обнаруживать асинхронные задания в приложениях
