from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_categories_view, name='all-categories'),
    path('<slug:cat_slug>/',
         views.all_categories_view,
         name='products-by-category')
]
