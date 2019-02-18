from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
# from django.views.generic import FormView
from django.views.generic import CreateView

from .models import Transaction


def signup(request):
    template_name = 'signup.html'
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST) # form with data
        if signup_form.is_valid():
            signup_form.save()
            return redirect('home')
    else:
        signup_form = UserCreationForm()

    context = {
        'form': signup_form,
    }
    return render(request,template_name, context)


# class based view use
class TransactionView(CreateView):
    model = Transaction
    template_name = 'transaction.html'
    fields = ('from_user', 'to_user', 'ammount')
    context_object_name = 'form'
    success_url = '/'

    