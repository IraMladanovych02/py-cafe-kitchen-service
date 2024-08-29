from django.urls import path

from cafe.views import (
    index,
    DishTypeListView,
    DishListView,
    DishDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookExperienceUpdateView,
    CookDeleteView,
    toggle_assign_to_dish,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-types-create"),
    path("dish_types/update/<int:pk>/", DishTypeUpdateView.as_view(), name="dish-types-update"),
    path("dish_types/delete/<int:pk>/", DishTypeDeleteView.as_view(), name="dish-types-delete"),

    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/update/<int:pk>/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/delete/<int:pk>/", DishDeleteView.as_view(), name="dish-delete"),

    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/update/<int:pk>/", CookExperienceUpdateView.as_view(), name="cook-update"),
    path("cooks/delete/<int:pk>/", CookDeleteView.as_view(), name="cook-delete"),
    path('dishes/toggle/<int:pk>/', toggle_assign_to_dish, name='toggle-assign-to-dish'),
]

app_name = "cafe"
