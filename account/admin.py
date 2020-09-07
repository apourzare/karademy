from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import User

UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'national_id', 'phone', 'email')
UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'national_id', 'is_staff')

# UserAdmin.fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone')}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )

admin.site.register(User, UserAdmin)

