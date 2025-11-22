# demo/urls.py
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # páginas
    path('', views.login_view, name='sesion'),
    path('index/', views.index, name='index'),
    path('templates/game.html/', views.Web_view, name='web'),
    path('challenges/', views.challenges_view, name='challenges'),
    path('resources/', views.resources_view, name='resources'),
    path('solutions/', views.solutions_view, name='solutions'),
    path('take-action/', views.takeaction_view, name='take-action'),

    # sesión / registro
    path('register/', views.register_view, name='registro'),
]
