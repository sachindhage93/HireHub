from django.urls import path
from . import views


urlpatterns = [

    path(
        'role-home/',
        views.role_home,
        name='role_home'
    ),

    path(
        'profile/',
        views.profile_view,
        name='profile'
    ),

    path(
        'profile/edit/',
        views.profile_edit,
        name='profile_edit'
    ),

]