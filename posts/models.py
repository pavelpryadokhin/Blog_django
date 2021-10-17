from django.db import models
from django.urls import reverse

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField('Заголовок',max_length=120)
    content=models.TextField('Текст')
    timestamp=models.DateTimeField('Дата создания',auto_now=False, auto_now_add=True )
    updated=models.DateTimeField('Дата обновления',auto_now=True, auto_now_add=False )
    post_likes=models.IntegerField(default=0)
    status=(('r1','Роман'),('p','Поэма'),('r2','Рассказ'),('s','Стих'))
    status= models.CharField('Жанр',choices=status,max_length=2,default='r1')
    post_author=models.ForeignKey('Author',on_delete=models.CASCADE,verbose_name='Автор поста',blank=True, null=True )
    image=models.ImageField('Картинкa',blank=True,null=True)

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'
        db_table='posts'#задали название в БД
        ordering=['-timestamp']#порядок

    def __str__(self):
        return self.title

    def get_url(self):
        # return '{}'.format(self.id)
        return reverse('posts:detail',kwargs={'id':self.id})

class Author(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField('Имя',max_length=120)
    second_name=models.CharField('Фамилия',max_length=120)
    email=models.EmailField('Почта',max_length=254)
    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'
        db_table='authors'
        ordering=['second_name','first_name']


    def __str__(self):
        return self.first_name+' '+self.second_name

class Comments(models.Model):
    id=models.AutoField(primary_key=True)
    comment_text=models.TextField('Комментарий')
    comment_article=models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name='Статья')
    timepublish=models.DateTimeField('Дата пуликации',auto_now=False, auto_now_add=True, blank=True, null=True )



    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'
        db_table='comments'


    def __str__(self):
        return self.comment_text