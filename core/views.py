from django.shortcuts import render ,redirect
from django.contrib.auth.views import LoginView
from farmer.models import Farmer
from public_user.models import Public_user


def home(request):
    return render(request,"core/opening.html")

class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user

        # Check if the user is a farmer
        if Farmer.objects.filter(user=user).exists():
            return '/farmerhome/'  # Redirect to Farmer's home page

        # Check if the user is a public user
        elif Public_user.objects.filter(user=user).exists():
            return '/userhome/'  # Redirect to Public user's home page

        # Default redirect (optional)
        return '/'

