from django.db import models


# class Contact(models.Model):
#     """Модель Контакта AmoCRM"""
#
#     # ФИО контакта
#     name = models.CharField(
#         max_length=255,
#         blank=False,
#         null=False,
#         default='Иванов Иван Иванович'
#     )
#     # Электронная почта контакта
#     email = models.EmailField(
#         blank=True,
#         null=False,
#         default='email@mail.com'
#     )
#     # Номер телефона, привязанного к контакту
#     phone = models.CharField(
#         max_length=15,
#         blank=True,
#         null=False,
#         default=''
#     )
#
#     # Метод для вывода полного названия объекта модели
#     def __str__(self):
#         return '%s %s %s' % (self.name, self.email, self.phone)
