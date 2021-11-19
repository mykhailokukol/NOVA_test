from django.shortcuts import render
from django.views.generic import View
from . import models


class IndexView(View):
    """Бизнес-логика обнаружения или создания
    пользователя AmoCRM"""

    def get(self, request):
        pass
