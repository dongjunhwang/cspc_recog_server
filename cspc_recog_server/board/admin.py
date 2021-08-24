from django.contrib import admin
from .models import *
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ['group_id', 'board_name']
    list_display_links = ['board_name']
    list_filter = ['group_id']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','GetGroupName','GetBoardName','title','author','like_count','has_image']
    list_display_links = ['id','title']

    def GetBoardName(self,obj):
        return obj.board_id.board_name
    GetBoardName.admin_order_field = 'board_id'
    GetBoardName.short_description = 'board name'
    def GetGroupName(self,obj):
        return obj.board_id.group_id
    GetGroupName.short_description = 'group name'

class PostImageAdmin(admin.ModelAdmin):
    list_display = ['post_name','id','image']

    def post_name(self,obj):
        return obj.post.title

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','post_name','author']

    def post_name(self,obj):
        return obj.post_id.title



admin.site.register(Board,BoardAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(PostImage,PostImageAdmin)
admin.site.register(Comment,CommentAdmin)