"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from blog import views as blog_views
from accounts import views as accounts_views
from messages import views as messages_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('about/', blog_views.about, name='about'),
    path('pages/', blog_views.pages, name='pages'),
    path('create_page/', blog_views.create_page, name='create_page'),
    path('update_page/<int:page_id>/', blog_views.update_page, name='update_page'),
    path('delete_page/<int:page_id>/', blog_views.delete_page, name='delete_page'),
    path('get_page/<int:page_id>/', blog_views.get_page, name='get_page'),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),
    path('signup/', accounts_views.signup_view, name='signup'),
    path('profile/', accounts_views.profile_view, name='profile'),
    path('profile/update/', accounts_views.update_profile_view, name='update_profile'),
    path('messages/', messages_views.message_list, name='message_list'),
    path('messages/create/', messages_views.create_message, name='create_message'),
    path('messages/<int:message_id>/', messages_views.view_message, name='view_message'),
]


