from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.entry, name='wiki_entry'),
    path('search/', views.search, name='search'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('random/', views.random_entry, name='random_entry'),
    path('edit_entry/<str:title>', views.edit_entry, name='edit_entry'),

]
