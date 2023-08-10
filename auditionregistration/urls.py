# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('auditionregi/', views.auditionregi, name='auditionregi'),
#     path('auditionregidata/', views.auditionregi_data, name='auditionregidata'),
#     path('deleteregidata<int:id>/', views.deleteregi_data, name='deleteregidata'),
#     path('updateregi<int:id>/', views.updateregi, name='updateregi'),
#     path('updateregidata<int:id>/', views.updateregi_data, name='updateregidata'),
    
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('insertimg', views.insertimg, name='insertimg'),
    path('auditionregi', views.auditionregi, name='auditionregi'),
    path('auditionregidata/', views.auditionregi_data, name='auditionregidata'),
    path('deleteregidata<int:id>/', views.deleteregi_data, name='deleteregidata'),
    path('updateregi<int:id>/', views.updateregi, name='updateregi'),
    path('updateregidata<int:id>/', views.updateregi_data, name='updateregidata'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
         