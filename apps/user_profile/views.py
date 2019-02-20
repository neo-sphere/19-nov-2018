from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.views.generic import CreateView

from .models import Transaction
from .forms import TransactionForm


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
    form_class = TransactionForm
    template_name = 'transaction.html'
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.from_user = self.request.user
        obj.save()
        return super().form_valid(form)

