from django.contrib import admin
from django.urls import path
from appdaaline import views

urlpatterns = [
    # path('', views.home),
    path('admin/', admin.site.urls),
    path("atv", views.create_atv),
    path("atv/update/<id>", views.update_atv),
    path("atv/delete/<id>", views.delete_atv),
    # path("lugar/update/<id>", views.update_lugar),
    path('', views.listagem, name="listagem")
]