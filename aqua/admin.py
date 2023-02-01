from django.contrib import admin
from .models import Aqua




@admin.register(Aqua)
class AdminAqua(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'app_name')
    search_fields = ('title', 'app_name')
