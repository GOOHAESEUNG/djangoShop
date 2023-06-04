from django.contrib import admin
from .models import User #user.models.User를 토대로 admin class 생성
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    #models.py/User에 있는 email &&주의사항('email',) 안에 ,를 안찍으면 튜플로 인식을 못함

admin.site.register(User,UserAdmin)