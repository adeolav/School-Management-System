from django.shortcuts import render
# Login required to access private pagas
from django.contrib.auth.decorators import login_required
# Prevent back button (destroy the last section)
from django.views.decorators.cache import cache_control

# Frontend
def frontend(request):
    """path for frontend function"""
    return render(request, "frontend.html")

# Backend
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    """path for backend function"""
    return render(request, "backend.html")