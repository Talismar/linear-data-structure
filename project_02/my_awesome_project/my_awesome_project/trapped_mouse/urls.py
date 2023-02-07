from django.urls import path

from my_awesome_project.trapped_mouse.views import (
    trapped_mouse_home
)

app_name = "trapped_mouse"
urlpatterns = [
    path("", view=trapped_mouse_home, name="home"),
]
