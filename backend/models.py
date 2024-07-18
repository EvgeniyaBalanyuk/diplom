from django.db import models

'''Модель категории товара'''


class Category(models.Model):
    name = models.CharField(max_length=200)  # Наименование категории
    slug = models.SlugField(max_length=200, unique=True)  # Создание индекса

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),  # Индекс определен по полю name
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


'''Модель товаров'''


class Product(models.Model):
    category = models.ForeignKey(Category,  # внешний ключ к модели Category, взаимосвязь один ко многим, товар принадлежит к одной категории, категория содержит несколько товаров
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  # Название товара
    slug = models.SlugField(max_length=200)  # Слаг этого товара, для создания красивых URL-адресов
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)    # Опциональное изображение товара
    description = models.TextField(blank=True)  # Опциональное описание товара
    price = models.DecimalField(max_digits=10,   # Цена товара, максимальное количество цифр
                                decimal_places=2)  # Десятичные разряды
    available = models.BooleanField(default=True)  # Наличие или отсутствие товара, используется для активирования/деактивирования товара в каталоге
    created = models.DateTimeField(auto_now_add=True)  # Дата/время создания объекта
    updated = models.DateTimeField(auto_now=True)  # Дата/время обновления объекта в последний раз

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),  # повышение производительности запросов
            models.Index(fields=['name']),  # индекс по полю name
            models.Index(fields=['-created']),  #  индекс по полю created определен в убывающем порядке
        ]

    def __str__(self):
        return self.name

