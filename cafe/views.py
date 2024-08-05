from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic

from cafe.models import DishType, Dish, Cook, Ingredients


def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_ingredients = Ingredients.objects.count()
    context = {
        "num_dish": num_dishes,
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients,
    }
    return render(request, "cafe/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish-types-list"
    queryset = DishType.objects.select_related("name")
    pagination = 5
    template_name = "cafe/dish_types_list.html"


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "cafe/dish_types_detail_list.html"


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish-list"
    queryset = Dish.objects.select_related("name")
    pagination = 5
    template_name = "cafe/dish_list.html"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "cafe/dish_detail_list.html"
