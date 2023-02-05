from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import AddPublicPost, ViewPublicPostDetail, ViewAllPublicPosts, AddUserPost, ViewUserPosts
 
urlpatterns = [
        path('', views.index, name ='index'),
        #publicposts
        path('addpublicpost/', AddPublicPost.as_view(), name="add_publicpost"),
        path('viewpublicpost/<int:pk>/', ViewPublicPostDetail.as_view(), name="view_publicpost"),
        path('viewallpublicposts/', ViewAllPublicPosts.as_view(), name="view_allpublicposts"),

        #userposts
        path('adduserpost/', AddUserPost.as_view(), name="add_userpost"),
        path('viewuserposts/', ViewUserPosts.as_view(), name="view_userposts"),
]