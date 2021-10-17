from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post,Author,Comments
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# вариант запроса  для справки..(старый вариант)
# from django.template.loader import get_template
# from django.template import Context
# def post_home(request):
#     home='Basic'
#     t=get_template('basic.html')
#     html=t.render(Context({'name':home}))
#     return HttpResponse(html)
#
# новый рабочий вариант, как надо (страничку пока не использую)
# def post_home(request):
#     content={
#         'title':'post_home',
#         'name':'Домашняя страничка'
#     }
#     return render(request,'basic.html',content)

def post_detail(request,id=None):
    instance=get_object_or_404(Post,id=id)
    content={
        'title':'post_detail',
        'instance':instance
    }
    return render(request, 'post_detail.html',content)



def post_create(request):
    # form=PostForm()
    # if request.method=='POST':
    #     title=request.POST.get('title')
    #     content=request.POST.get('content')
    #     status=request.POST.get('status')
    #     post_author=request.POST.get('post_author')
    #     Post.objects.create(title=title,content=content,status=status,post_author=Author.objects.get(id=post_author))
    form=PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,'<a href="#">Успешно создано</a>',extra_tags='ok_h')
        return HttpResponseRedirect(instance.get_url())
    content={
        'title':'post_create',
        'name':'Создание поста',
        'form':form,
        'val_but':'Создать'
    }
    return render(request, 'post_create.html',content)


def post_update(request, id=None):
    instance=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "Успешно отредактировано ",extra_tags='ok')
        return HttpResponseRedirect(instance.get_url())
    content={
        'title':'post_update',
        'name':'Редактирование поста',
        'form':form,
        'val_but':'Редактировать'
    }
    return render(request, 'post_create.html',content)


def post_delete(request,id=None):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request, "Успешно удалено",extra_tags='del')
    return redirect('posts:list')


def post_list(request):
    if request.user.is_authenticated:
        authenticated='Авторизированный пользователь'
    else:
        authenticated='Гость'

    queryset_list=Post.objects.all()
    paginator=Paginator(queryset_list,2)
    page_name='page'
    page=request.GET.get(page_name)
    try:
        queryset=paginator.get_page(page)
    except PageNotAnInteger:
        queryset=paginator.get_page(1)
    except EmptyPage:
        queryset=paginator.get_page(paginator.num_pages)
    content={
        'title':'post_list',
        'name':'Мой блог',
        'user':authenticated,
        'queryset':queryset
    }
    return render(request,'post_list.html',content)



