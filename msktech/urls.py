from django.contrib import admin
from django.urls import path, include
from techapp import views as user_view
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
 
    path('admin/', admin.site.urls),
 
    ##### user related path##########################
    path('', include('techapp.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('login/', user_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', user_view.register, name ='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('summernote/', include('django_summernote.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)