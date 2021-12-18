from django.shortcuts import render
from members.forms import RegistrationForm
from django.http import HttpResponseRedirect

def register_user_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/members/login')
        return render(request, 'registration/register.html', {'form':form})

    form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})


