from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('auth/', include('user.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
