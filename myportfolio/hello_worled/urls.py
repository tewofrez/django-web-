from django.urls import path
from . import views
app_name = "hewwlo"
urlpatterns = [
    path("", views.index, name="index")
]
