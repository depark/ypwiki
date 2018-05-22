from django.db import models
from django.contrib.auth.models import User,Group
from DjangoUeditor.models import UEditorField


# Create your models here.


class Project(models.Model):
    '''
    projects
    项目情况

    '''
    name=models.CharField('项目名',max_length=128,null=False,unique=True)
    intr=models.TextField('项目介绍')
    owner=models.CharField('项目负责人',max_length=128,null=False)
    create_time=models.DateTimeField('项目创建时间',auto_now=True)


    def __str__(self):
        return self.name


class Article(models.Model):
        '''
        wenzhang
        '''
        title=models.CharField(verbose_name='文档标题',max_length=128,unique=True)
        context=UEditorField(verbose_name='文档内容',height=300, width=1000,
        default='', blank=True, imagePath="news/",
        toolbars='full', filePath='files')
        create_user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='文档创建人',related_name='create_user')
        create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
        last_update_user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='最近更新人',related_name='last_update_user')
        last_update_time = models.DateTimeField(verbose_name='最近更新时间',auto_now=True)
        belong=models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='所属项目')

        def __str__(self):
            return self.title


class  Sum(models.Model):
    '''huizong'''

    name = models.CharField(max_length=128, unique=True)
    create_num=models.IntegerField()
    update_num = models.IntegerField()

    def __str__(self):
        return self.name
