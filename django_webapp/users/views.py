from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    # create an instance of the form and render the template that uses the form
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get("first_name")
            messages.success(request, f'{first_name}, your account has been created. You are now able to login')
            return redirect('login')  # you can choose to redirect users to home page or login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm (request.POST,
                                    request.FILES, 
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = CustomUserChangeForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form

    }

    return render(request, 'users/profile.html', context)