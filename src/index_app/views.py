from django.shortcuts import render
from django.views.generic import View
# from django.core.exceptions import ObjectDoesNotExist
from . import models
from . import forms
import requests
import json


class IndexView(View):
    """Бизнес-логика обнаружения или создания
    пользователя AmoCRM"""

    def get(self, request):
        
        return render(request, 'index_app/index.html', {

        })
