from django.shortcuts import render
from homepage.models import Recipe

# Create your views here.
def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes, "welcome_name": "USER"})

def post_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post_id": my_recipe})