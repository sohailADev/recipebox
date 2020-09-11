from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Recipe, Author
from django.contrib.auth.decorators import login_required
from homepage.forms import RecipeForm, AuthorForm, LoginForm, SignupForm,EditRecipeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    my_recipes = Recipe.objects.all()    
    return render(request, "index.html", {"recipes": my_recipes, "welcome_name": "USER"})

def fav_recipe_view(request,user_id):   
    logged_in_user = Author.objects.get(id=user_id)    
    my_recipes = logged_in_user.fav_recipies.all()       
    return render(request, "fav_recipes.html", {"recipes": my_recipes, "welcome_name": "USER"})

def post_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": my_recipe})

def add_favorite_recipe_view(request, recipe_id):
    fav_recipe = Recipe.objects.get(id=recipe_id)
    logged_in_user = Author.objects.get(user=request.user)
    logged_in_user.fav_recipies.add(fav_recipe)
    logged_in_user.save() 
    return HttpResponseRedirect(reverse("homepage"))

@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():                
            data = form.cleaned_data      
            signup_user = User.objects.create_user(
                username = data.get('name'),
                password=data.get('password')
                )
            Author.objects.create(
                name = data.get('name'),
                bio = data.get('bio'),
                user= signup_user
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AuthorForm()
    return render(request, "genericform.html", {"form": form})


@login_required
def add_recipe_form(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                author=request.user.author,
                time_required=data.get('time_required'),
                instructions=data.get('instructions'),
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = RecipeForm()
    return render(request, "genericform.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
            else:
                return HttpResponseRedirect(reverse("loginview"))

    form = LoginForm()
    return render(request, "genericform.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get(
                "username"), password=data.get("password"))
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


def edit_recipe_view(request, recipe_id):
      recipe_edit = Recipe.objects.get(id=recipe_id)
      if request.method == 'POST':
            form = EditRecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data     
                recipe_edit.title = data['title']
                recipe_edit.description = data["description"]
                recipe_edit.author = data["author"]
                recipe_edit.time_required = data["time_required"]
                recipe_edit.instructions = data["instructions"]
                recipe_edit.save()
            return HttpResponseRedirect(reverse("homepage"))
      data = {
            "title": recipe_edit.title,
            "author": recipe_edit.author,
            "description": recipe_edit.description,
            "time_required": recipe_edit.time_required,
            "instructions": recipe_edit.instructions,
        }
      form = EditRecipeForm(initial=data)
      return render(request, "genericform.html", {"form": form} )

def author_detail(request,author_id):
    _author_detail =Recipe.objects.filter(author__id= author_id)
    _author_name =Author.objects.get(id= author_id)
  
    
    context = {
        "author_detail":_author_detail,
        "author_name":_author_name
    }
    return render(request,'author_detail.html',context)