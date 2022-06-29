from django.contrib import admin
from .models import Post,Category,Tag

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
admin.site.register(Category,CategoryAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
admin.site.register(Tag,TagAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','feature')
admin.site.register(Post,PostAdmin)
