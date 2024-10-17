from django.urls import path
# from . import views
from .views import  HomeView, PostDetailView, AddPostView, AboutView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, TeamView, ContactView



urlpatterns = [
   # path('', views.home, name="home"),
   path('', HomeView.as_view(), name="home"),
   path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
   path('add_post/', AddPostView.as_view(), name='add_post'),
   path('add_category/', AddCategoryView.as_view(), name='add_category'),
   path('about_page/', AboutView.as_view(), name='about_page'),
    path('team_page/', TeamView.as_view(), name='team_page'),
    path('contact_page/', ContactView.as_view(), name='contact_page'),
   path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
   path('post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
   path('category/<str:cats>', CategoryView, name='category'),
   path('category-list/', CategoryListView, name='category-list'),
   path('like/<int:pk>', LikeView, name='like_post'),
   # path('cat_menu/<str:cats>', get_context_data, name='cat_menu')
]
