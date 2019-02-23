from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError

from django.views.generic import FormView
from django.views.generic import CreateView, DetailView

from .models import Transaction, Profile, Account
from .forms import TransactionForm, CustomUserCreationForm

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        mobile = form.cleaned_data.get('mobile') # cleaned_data dictinary ho
        Profile.objects.create(user=user, mobile=mobile)
        Account.objects.create(user=user)
        return super().form_valid(form)

# class based view use
class TransactionView(CreateView):
    form_class = TransactionForm
    template_name = 'transaction.html'
    success_url = '/'

    def form_valid(self, form):
        to_mobile = form.cleaned_data.get('to_mobile')
        if self.request.user.profile.mobile ==  to_mobile:
            raise ValidationError('balance cant transfer to self')
        obj = form.save(commit=False)
        obj.from_user = self.request.user
        obj.to_user = Profile.objects.get(mobile=to_mobile).user
        obj.save()
        return super().form_valid(form)

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        if self.request.user.id:
            queryset = queryset.filter(pk=self.request.user.id) #filter loggedin user 
            obj = queryset.get()
            return obj