from django.contrib import admin
from django.urls import path, include
from core.views import splash, read

urlpatterns = [
    path('admin/', admin.site.urls),
    path('read/', read, name='read'),
    path('', splash, name='splash')
]