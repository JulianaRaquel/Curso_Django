from django.urls import path

from pypro32.base.views import home

app_name='base'
urlpatterns = [
    path('', home, name='home'),
]