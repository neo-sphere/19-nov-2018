from datetime import date

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('address', 'dob', 'mobile', 'country', 'gender', 'profession', 'get_age')
    list_display_links = ('address', 'mobile')
    list_editable = ('dob', 'country')
    list_filter = ('gender',)
    search_fields = ('address', 'mobile', 'profession')

    def get_age(self, instance):
        age = date.today() - instance.dob
        return int(age.days//365.25)

    get_age.short_description = 'Age'

# admin.site.register(Profile, ProfileAdmin) # old way
