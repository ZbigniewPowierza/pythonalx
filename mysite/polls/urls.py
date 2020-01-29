from django.urls import path

from polls import admin
from polls.views import index, funkcja_widoku, hello_name

urlpatterns = [
    path ("", index, name="index"),
    path ('hello/', funkcja_widoku),
    path ('hello/<name>', hello_name),
    path ("questions/",


]