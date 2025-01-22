from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .models import Profile
from .forms import ProfileForm


# Create your views here.

# Profile view
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

# Profile update view
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile

# Sign-up view
def signup(request):
    form = CustomSignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(request)
        return redirect('success')
    return render(request, 'accounts/signup.html', {'form': form})