from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# Here we are using djangos user creation form to let our users sign up
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # This saves the form
        if form.is_valid():
            form.save() # This saves the form and user
            username = form.cleaned_data.get("username")
            messages.success(request,f'Account created for {username}! You are now able to Login!') # After all the info is said we redirect to home page
            return redirect('login')

    else:
        form = UserRegisterForm()
        # Here we are not doing anything with the data
        # We created the form with post method so we have to validate that data and save it

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account has been updated!')  # After all the info is said we redirect to home page
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request,'users/profile.html',context)

