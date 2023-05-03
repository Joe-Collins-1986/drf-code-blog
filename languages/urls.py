from django.urls import path
from languages import views

urlpatterns = [
    path('', views.LanguageList.as_view()),
    path('<int:pk>/', views.LanguageDetail.as_view()),
]
