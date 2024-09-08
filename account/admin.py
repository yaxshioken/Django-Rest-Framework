from django.contrib import admin

from account.models import User, Profile, Interest


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','city','passport_number','passport_letter')
    list_filter = ('user','city','passport_number','passport_letter')
@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
