from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', views.sign_up, name='signup'),     
    path('login/', views.log_in, name='login'), 
    path('logout/', views.log_out, name='logout'), 
    path('profile/', views.profile, name='profile'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)