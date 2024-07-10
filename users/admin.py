from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    list_filter = ('profile__user_type',)  # Add filter for user_type

    def user_type(self, obj):
        return obj.profile.user_type
    user_type.admin_order_field = 'profile__user_type'
    user_type.short_description = 'User Type'

    # Add user_type to the list display
    def get_list_display(self, request):
        return self.list_display + ('user_type',)


# Re-register UserAdmin
admin.site.unregister(User)


admin.site.register(User, CustomUserAdmin)
