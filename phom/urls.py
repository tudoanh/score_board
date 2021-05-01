from django.urls import path
from .views import PhomHome

app_name = "phom"

urlpatterns = [
    path("phom/", PhomHome.as_view()),
]
