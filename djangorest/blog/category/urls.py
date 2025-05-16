from django.urls import path

from category.views import get_categories


urlpatterns = [path("", get_categories)]
