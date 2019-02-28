from django.urls import path, include
from . import views


# routing paths to specific functions
urlpatterns = [
    path("", views.index, name='index'),
    path("create/", views.create, name='create'),
    path("create/edit/<int:id>", views.editThis, name='edit'),
    path("create/delete/<int:id>", views.deleteThis, name='delete'),

]