from django.shortcuts import render,render_to_response
from wiki.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    title='wiki系统'
    #项目列表
    pros=Project.objects.all()

    #最新5篇文章
    last_docs=Article.objects.order_by('-id')[:5]

    #系统介绍
    intro=Article.objects.get(title='系统介绍')

    return render_to_response('index.html',locals())


def artshow(request,aid):
    doc= Article.objects.get(id=aid)

    pros = Project.objects.all()


    # 最新5篇文章
    last_docs = Article.objects.order_by('-id')[:5]

    #上一篇
    try:
        bdoc=Article.objects.get(id=int(aid)-1)
    except ObjectDoesNotExist as e:
        bdoc=''

    #下一篇
    try:
        adoc=Article.objects.get(id=int(aid)+1)
    except ObjectDoesNotExist as e:
        adoc=''
    return render_to_response('docshow.html', locals())


def proshow(request,pid):
    title='银票wiki'

    pro = Project.objects.get(id=pid)

    docs=Project.objects.get(id=pid).article_set.all()

    pros = Project.objects.all()

    # 最新5篇文章
    last_docs = Article.objects.order_by('-id')[:5]

    return render_to_response('proshow.html',locals())


