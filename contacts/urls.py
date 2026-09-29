from django.urls import path

from .views import *

urlpatterns = [
    path("contacts/", ContactList.as_view()),
    path("contacts/create/", ContactCreate.as_view()),
    path("contacts/<int:pk>/", ContactDetail.as_view()),
    path("contacts/<int:pk>/update/", ContactUpdate.as_view()),
    path("contacts/<int:pk>/patch/", ContactPartialUpdate.as_view()),
    path("contacts/<int:pk>/delete/", ContactDelete.as_view()),
]