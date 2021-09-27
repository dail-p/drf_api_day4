from django.db import models
from picklefield.fields import PickledObjectField


class CustomPickledObjectField(PickledObjectField):
    """
    Переопределен для корректного вывода в браузер
    """
    def value_to_string(self, obj):
        return self.value_from_object(obj)


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # график известности автора по годам.
    # поле состоит из словоря (год = кол.просмотров всех книг)
    fame = CustomPickledObjectField(default=dict)


class Book(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    authors = models.ManyToManyField('Author')
    # график популярности книги по годам.
    # поле состоит из словоря tuple-ов (год = кол.просмотров)
    fame = CustomPickledObjectField(default=dict)