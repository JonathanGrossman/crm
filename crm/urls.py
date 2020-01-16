
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('students.urls')),
    path('', include('data.urls')),
    path('admin/', admin.site.urls),
]
