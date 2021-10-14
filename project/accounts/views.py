from django.views import View
from django.shortcuts import redirect, render
from .forms import RegisterForm


class SignupView(View):
    def get(self, request):
        data = {"form": RegisterForm()}
        return render(request, "registration/register.html", data)
    
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:list')

        data = {
            'form':form
        }
        return render(request, 'registration/register.html', data)

