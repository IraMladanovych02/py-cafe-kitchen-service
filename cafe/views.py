from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from cafe.models import DishType, Dish, Cook
from cafe.forms import CookCreationForm, CookYearOfExperienceUpdateForm, DishForm


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_dish": num_dishes,
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_visits": num_visits + 1,
    }
    return render(request, "cafe/index.html", context=context)


class DishTypeListCreateView(LoginRequiredMixin, View):
    template_name = "cafe/dish_types_list.html"

    def get(self, request, *args, **kwargs):
        dish_types_list = DishType.objects.all()
        return render(request, self.template_name, {"dish_types_list": dish_types_list})

    def post(self, request, *args, **kwargs):
        dish_type_name = request.POST.get("name")
        if dish_type_name:
            DishType.objects.create(name=dish_type_name)
            return redirect("cafe:dish-types-list")
        dish_types_list = DishType.objects.all()
        return render(request, self.template_name, {"dish_types_list": dish_types_list})


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("cafe:dish-types-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "cafe/dish_types_delete_confirmation.html"
    success_url = reverse_lazy("cafe:dish-types-list")


class DishListCreateView(LoginRequiredMixin, View):
    template_name = "cafe/dish_list.html"

    def get(self, request, *args, **kwargs):
        dish_list = Dish.objects.all()
        return render(request, self.template_name, {"dish_list": dish_list})

    def post(self, request, *args, **kwargs):
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cafe:dish-list")
        dish_list = Dish.objects.all()
        return render(request, self.template_name, {"dish_list": dish_list, "form": form})


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("cafe:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("cafe:dish-list")
    template_name = "cafe/dish_delete_confirmation.html"


class CookListCreateView(LoginRequiredMixin, View):
    template_name = "cafe/cook_list.html"

    def get(self, request, *args, **kwargs):
        cook_list = Cook.objects.all()
        return render(request, self.template_name, {"cook_list": cook_list})

    def post(self, request, *args, **kwargs):
        form = CookCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cafe:cook-list")
        cook_list = Cook.objects.all()
        return render(request, self.template_name, {"cook_list": cook_list, "form": form})


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "cafe/cook_confirm_delete.html"
    success_url = reverse_lazy("cafe:cook-list")


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookYearOfExperienceUpdateForm
    template_name = "cafe/cook_form.html"
    success_url = reverse_lazy("cafe:cook-list")


@method_decorator(login_required, name='dispatch')
class ToggleAssignToDishView(View):
    def get(self, request, pk):
        cook = get_object_or_404(Cook, id=request.user.id)
        dish = get_object_or_404(Dish, id=pk)

        if dish in cook.dish.all():
            cook.dish.remove(dish)
        else:
            cook.dish.add(dish)

        return HttpResponseRedirect(reverse_lazy("cafe:cook-detail", args=[cook.id]))
