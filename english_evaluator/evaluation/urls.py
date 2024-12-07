from django.urls import path
from .views import RegisterView, LoginView, QuestionListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('questions/', QuestionListView.as_view(), name='questions'),
]
