from django.shortcuts import render, redirect

from django.views.generic import FormView
from django.views.generic import CreateView

from .models import Transaction, Profile, Account
from .forms import TransactionForm, CustomUserCreationForm

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        mobile = form.cleaned_data['mobile']
        Profile.objects.create(user=user, contact_no=mobile)
        Account.objects.create(user=user)
        return super().form_valid(form)

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

