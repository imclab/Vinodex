from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from registration.backends.simple.views import RegistrationView
from wine.models import UserProfile
from wine.forms import NewUserRegistrationForm

@login_required
def home(request):
    return render(request,"inventory.html")

class NewUserRegistrationView(RegistrationView):
    form_class = NewUserRegistrationForm

    def create_profile(self, request, user, **cleaned_data):
        first_name, last_name, avatar = (cleaned_data["first_name"],
        cleaned_data["last_name"], cleaned_data.get("avatar"))
        profile = UserProfile(user = user, first_name=first_name, last_name = last_name,
                avatar = avatar)
        profile.save()
        return profile

    def form_valid(self, request, form):
        new_user = self.register(request, **form.cleaned_data)
        new_user.profile = self.create_profile(request, new_user, **form.cleaned_data)
        new_user.save()
        success_url = self.get_success_url(request, new_user)
        
        # success_url may be a simple string, or a tuple providing the
        # full argument set for redirect(). Attempting to unpack it
        # tells us which one it is.
        try:
            to, args, kwargs = success_url
            return redirect(to, *args, **kwargs)
        except ValueError:
            return redirect(success_url)
