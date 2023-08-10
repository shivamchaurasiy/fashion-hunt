
from django.contrib import admin
from django.urls import path, include
# from huntapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('huntapp.urls')),
    path('', include('audition.urls')),
    path('', include('signup.urls')),
    path('', include('feedback.urls')),
    path('', include('contact.urls')),
    path('', include('auditionregistration.urls')),
]
    