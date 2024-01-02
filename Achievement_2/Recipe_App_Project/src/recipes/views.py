from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe


# Create your views here.
def home_view(request):
    return render(request, "recipes/main_home.html")


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipes_home.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail_page.html"
