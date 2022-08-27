from django.contrib import admin
from django.urls import path
from brasileirao.views import TabelaListViewset

urlpatterns = [
    path('', TabelaListViewset.as_view()),
]
