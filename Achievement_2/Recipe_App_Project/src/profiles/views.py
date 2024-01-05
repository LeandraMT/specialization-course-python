from django.shortcuts import render
from .models import Profile

# Protecting Function-based View
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "profile/profile_view.html", {"profile": profile})
