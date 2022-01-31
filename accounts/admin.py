from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):

    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    list_display = ['username','password','age','email']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('age',)}),
    )


admin.site.register(CustomUser,CustomUserAdmin)
