from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('blogs/', BlogVeiw, name='blogs'),
    path('blogs/<slug:slug>', blogPostView, name='blog_post'),
    path('contact/', contactView, name='contact'),
    path('about/', aboutView, name='about'),
    path('search/', searchView, name='search'),
    path('categories/', categoriesView, name='categories'),
    path('categories/<slug:slug>/', postCategoriesView, name='post_categories'),
    path('tags/', tagsView, name='tags'),
    path('tags/slug:slug>', postTagView, name='post_tag'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/delete/', DeleteProfileView.as_view(), name='delete_profile'),
    path('addblog/', addBlog, name='addblog'),
]