from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            firstName = form.cleaned_data.get('first_name')
            lastName = form.cleaned_data.get('last_name')
            messages.success(request, f'Conta criada com sucesso, {firstName} {lastName}!')
            return redirect('home')
    else:
       form = UserRegisterForm() 
    return render(request, 'users/register.html', {'form': form})
