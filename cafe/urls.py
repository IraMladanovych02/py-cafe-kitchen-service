from django.urls import path

from cafe.views import (
    index,
    DishTypeListCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishDetailView,
    DishListCreateView,
    DishUpdateView,
    DishDeleteView,
    CookDetailView,
    CookListCreateView,
    CookExperienceUpdateView,
    CookDeleteView,
    ToggleAssignToDishView,
)


urlpatterns = [
    path("", index, name="index"),

    path("dish_types/", DishTypeListCreateView.as_view(), name="dish-types-list"),
    path("dish_types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-types-update"),
    path("dish_types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-types-delete"),

    path("dish/", DishListCreateView.as_view(), name="dish-list"),
    path("dish/<int:pk>/detail", DishDetailView.as_view(), name="dish-detail"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),

    path("cooks/", CookListCreateView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/detail/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", CookExperienceUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),

    path('dishes/<int:pk>/toggle/', ToggleAssignToDishView.as_view, name='toggle-assign-to-dish'),
]

app_name = "cafe"
