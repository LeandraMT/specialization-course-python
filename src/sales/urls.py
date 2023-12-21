from django.urls import path
from .views import home

# Specifying the app name
app_name = "sales"

# Specifying the urls
urlpatterns = [
    path("", home),
]
