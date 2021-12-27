from django.contrib import admin
from .models import CustomUser
# Register your models here.


class CustomUserAdminConfig(CustomUser):
    ordering = ('-start_date',)
    list_display = ('email','username','is_active','is_staff')
    fieldsets = (
        (None,{
            'fields':('email','username')
        }),
        ('Permission',{
            'fields':('is_active','is_staff')
        })
    )


admin.site.register(CustomUser)



