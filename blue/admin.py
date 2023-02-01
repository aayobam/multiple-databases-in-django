from django.contrib import admin
from .models import Blue




# @admin.register(Blue)
# class AdminBlue(admin.ModelAdmin):
#     list_display = ('id', 'title', 'content', 'app_name')
#     search_fields = ('title', 'app_name')


class AdminBlue(admin.ModelAdmin):
    using = 'blue_db'
    
    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def save_model(self, request, obj, form, change):
        return obj.save(using=self.using)

    def delete_model(self, request, obj):
        return obj.delete(using=self.using)
    
    list_display = ('id', 'title', 'content', 'app_name')
    search_fields = ('title', 'app_name')


admin.site.register(Blue, AdminBlue)
