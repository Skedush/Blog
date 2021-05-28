from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserInfo
from django.utils.translation import gettext_lazy

# Register your models here.


class UserInfoInline(admin.StackedInline):
    model = UserInfo


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        (gettext_lazy('Personal info'), {
         'fields': ('first_name', 'last_name', 'email', 'gender',)}),
        (gettext_lazy('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_delete'),
        }),
        (gettext_lazy('Important dates'), {
         'fields': ('last_login', 'date_joined')}),
    ]
    # 添加user时可以直接添加userinfo
    inlines = (UserInfoInline, )

    list_per_page = 10
    ordering = ('-id',)


@ admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'home', 'git', 'motton', 'user')
    list_display_links = ['user', ]
    search_fields = ['phone', 'user__username']
    list_per_page = 10
    ordering = ('-user',)
