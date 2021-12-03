from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class Admin(admin.ModelAdmin):
    list_display = ('__str__', 'complete')
    search_fields = ('description',)
    list_filter = ('complete',)