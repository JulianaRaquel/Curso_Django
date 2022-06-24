
from django.contrib import admin
from django.urls import path
#from pypro32.base.views import home
from pypro32.base.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]
