from django.urls import path

from cafe.views import (
    index,
    DishTypeListView,
    DishListView,
    DishTypeDetailView,
    DishDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypeListView.as_view, name="dish-types-list"),
    path("dish_types/<int:pk>/", DishTypeDetailView.as_view, name="dish-types-detail"),
    path("dish/", DishListView.as_view, name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view, name="dish-detail"),
]

app_name = "cafe"
