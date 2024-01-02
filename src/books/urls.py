from django.urls import path
from .views import BookListView

# Specifying the app name
app_name = "books"

# Specifying the urls
urlpatterns = [path("books/", BookListView.as_view(), name="book-list")]
