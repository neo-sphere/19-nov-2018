from datetime import date

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Transaction, Account

admin.site.unregister(User)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Account'
    fk_name = 'user'

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, AccountInline)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ('user', 'balance', 'point')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'ammount', 'created')
