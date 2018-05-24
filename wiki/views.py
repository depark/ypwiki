from django.shortcuts import render,render_to_response,HttpResponseRedirect,reverse
from wiki.models import *
from django.core.exceptions import ObjectDoesNotExist
from wiki.api import *

# Create your views here.


def index(request):
    title='wiki系统'
    #项目列表
    pros=Project.objects.all()

    #最新5篇文章
    last_docs=Article.objects.order_by('-id')[:5]

    # 系统介绍
    doc = Article.objects.get(title='系统介绍')

    #上一篇和下一篇
    bdoc,adoc = lastdoc(doc.id)



    return render_to_response('docshow.html',locals())
    #return HttpResponseRedirect(reverse(artshow,args=[intro.id]))

def artshow(request,aid):
    doc= Article.objects.get(id=aid)

    pros = Project.objects.all()


    # 最新5篇文章
    last_docs = Article.objects.order_by('-id')[:5]

    #上一篇和下一篇
    bdoc,adoc = lastdoc(aid)
    return render_to_response('docshow.html', locals())


def proshow(request,pid):
    title='银票wiki'

    pro = Project.objects.get(id=pid)

    docs=Project.objects.get(id=pid).article_set.all()

    pros = Project.objects.all()

    # 最新5篇文章
    last_docs = Article.objects.order_by('-id')[:5]

    return render_to_response('proshow.html',locals())


