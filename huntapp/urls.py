
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('cateform/', views.cate_form, name='cateform'),
    path('categorydata/', views.categorydata, name='categorydata'),
    path('update<int:id>/', views.update_data, name='update'),
    path('delete<int:id>/', views.delete_data, name='delete'),
]
