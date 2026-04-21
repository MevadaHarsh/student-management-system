from django.urls import path
from .views import *


urlpatterns = [
    path('form', form, name="form"),
    path('', st_ls, name="st_ls"),
    path('st_up/<int:id>', st_up, name="st_up"),
    path('st_del/<int:id>', st_del, name="st_del"),
]
