from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
app_name = 'main'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('post/<str:slug>', PostView.as_view(), name = 'post'),
    path('category/<str:slug>', CategoryDetailView.as_view(), name='category'),

    path('admins/create/', AdminPostCreateView.as_view(), name='create_post'),
    path('admins/<int:pk>/delete/',
         AdminPostDeleteView.as_view(), name='delete_post'),
    path('adminedit/<int:pk>/', AdminPostUpdateView.as_view(), name='edit_post'),
    path('search/', SearchView.as_view(), name = 'search'),
    path('admins/post/', AdminPostListView.as_view(), name='list_post'),
    path('post/<str:slug>/', PostView.as_view(), name='post'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category'),

    path('admins/create', AdminPostCreateView.as_view(), name='create_post'),
    path('admins/<int:pk>/delete',
         AdminPostDeleteView.as_view(), name='delete_post'),
    path('adminedit/<int:pk>', AdminPostUpdateView.as_view(), name='edit_post'),
    path('search', SearchView.as_view(), name='search'),
    path('admins/post/', AdminPostListView.as_view(), name='list_post'),

]