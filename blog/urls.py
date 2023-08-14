from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('create_page/', views.create_page, name='create_page'),
    path('update_page/<int:page_id>/', views.update_page, name='update_page'),
    path('delete_page/<int:page_id>/', views.delete_page, name='delete_page'),
    path('get_page/<int:page_id>/', views.get_page, name='get_page'),
    path('about_me/', views.about_me, name='about_me'),
]