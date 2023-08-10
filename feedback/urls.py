from django.urls import path
from . import views

    
urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('feedbackdata/', views.feedback_data, name='feedbackdata'),
]
