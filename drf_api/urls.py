from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('profiles/', include('profiles.urls')),
    path('articles/', include('articles.urls')),
    path('comments/', include('comments.urls')),
    path('likes/', include('likes.urls')),

]
