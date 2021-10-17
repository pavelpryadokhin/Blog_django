from django.contrib import admin

from .models import Post
from .models import Author
from .models import Comments

class PostInstanceInline(admin.StackedInline):
    model=Comments
    extra=1

class PostAdmin(admin.ModelAdmin):
    list_display=['title','timestamp','updated','status']#Для отображения списка полей, выводимых в части администратора
    list_display_links=['updated']#Для отображения списка полей ссылками, выводимых в части администратора
    list_filter=['title','updated']#Для отображения фильтра, выводимого в части администратора
    search_fields=['title','content']#Для отображения поиска, выводимого в части администратора
    list_editable=['title']#создание редактируемых полей
    inlines=[PostInstanceInline]
    #field=('title',) #что хотим что бы отображалось
    exclude=('post_likes',)#что не хотим что бы отображалось
    

    class Meta:
        model=Post


class AuthorInstanceInline(admin.StackedInline):
    model=Post
    extra=0
    fields = ("title",'content')

class AuthorAdmin(admin.ModelAdmin):
    list_display=['first_name','second_name','email']#Для отображения списка полей, выводимых в части администратора
    list_display_links=['first_name']#Для отображения списка полей ссылками, выводимых в части администратора
    search_fields=['first_name','second_name']#Для отображения поиска, выводимого в части администратора
    list_editable=['email']#создание редактируемых полей
    inlines=[AuthorInstanceInline]
    class Meta:
        model=Author


class CommentsAdmin(admin.ModelAdmin):
    list_display=['comment_text','comment_article']#Для отображения списка полей, выводимых в части администратора
    list_display_links=['comment_text']#Для отображения списка полей ссылками, выводимых в части администратора
    search_fields=['comment_text','comment_article']#Для отображения поиска, выводимого в части администратора
    list_filter=['timepublish']
    class Meta:
        model=Comments

admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Comments,CommentsAdmin)


