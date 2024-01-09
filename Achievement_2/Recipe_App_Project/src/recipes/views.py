from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Recipe


# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_home.html"


def home_view(request):
    return render(request, "recipes/main_home.html")


def search_view(request):
    query = request.GET.get("q")
    object_list = Recipe.objects.filter(
        Q(name__icontains=query) | Q(ingredients__icontains=query)
    )
    return render(request, "recipes/recipes_list.html", {"object_list": object_list})


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail_page.html"
