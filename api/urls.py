from django.contrib import admin
from django.urls import path, include

from api.view import TranslateTextApi

urlpatterns = [
    path('translate-text/', TranslateTextApi.as_view({'get': 'list'})),
]
