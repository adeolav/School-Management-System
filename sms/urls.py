from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Frontend
    path('', views.frontend, name="frontend"),
    # Backend
    path('backend/', views.backend, name="backend"),
    # Login/Logout
    path('login/', include('django.contrib.auth.urls')),
]