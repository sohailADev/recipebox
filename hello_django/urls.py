"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('favorite/<int:user_id>/', views.fav_recipe_view, name="fav_recipe_page"),
    path('addfavorite/<str:recipe_id>/', views.add_favorite_recipe_view, name="add_fav_recipe_page"),
    path('post/<int:post_id>/', views.post_detail,name="recipe_detail_page"),
    path('author/<int:author_id>/', views.author_detail,name="author_detail_page"),
    path('newrecipe/', views.add_recipe_form, name="newrecipe"),
    path('newauthor/', views.add_author, name="newauthor"),
    path('editrecipe/<int:recipe_id>/', views.edit_recipe_view, name="edit_recipe"),
    path('login/', views.login_view, name="loginview"),
    path('logout/', views.logout_view, name = "logoutview"),
    path('signup/', views.signup_view, name="signup"),
    path('admin/', admin.site.urls),
]
