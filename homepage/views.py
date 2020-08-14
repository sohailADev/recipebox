from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Recipe
from homepage.forms import RecipeForm, AuthorForm

# Create your views here.


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes, "welcome_name": "USER"})


def post_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": my_recipe})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AuthorForm()
    return render(request, "genericform.html", {"form": form})


def add_recipe_form(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                author=data.get('author'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions'),
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = RecipeForm()
    return render(request, "genericform.html", {"form": form})
