from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('News.urls')),
    path('new', include('News.urls')),
    path('admin/', admin.site.urls),
]



