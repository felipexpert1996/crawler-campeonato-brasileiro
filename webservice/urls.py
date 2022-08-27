import imp
from django.contrib import admin
from django.urls import path
from brasileirao.views import TabelaListViewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TabelaListViewset.as_view())
]
