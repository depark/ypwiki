from django.db import models
from django.contrib.auth.models import User,Group
from DjangoUeditor.models import UEditorField


# Create your models here.


class Project(models.Model):
    '''
    projects

    '''
    name=models.CharField(max_length=128,null=False,unique=True)
    intr=models.TextField()
    owner=models.CharField(max_length=128,null=False)
    create_time=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Article(models.Model):
        '''
        wenzhang
        '''
        title=models.CharField(max_length=128,unique=True)
        context=UEditorField(height=300, width=1000,
        default='', blank=True, imagePath="news/",
        toolbars='full', filePath='files')
        create_user=models.ForeignKey(User)
        create_time = models.DateTimeField(auto_now_add=True)
        #last_update_user = models.ForeignKey(User)
        last_update_time = models.DateTimeField(auto_now=True)
        belong=models.ForeignKey(Project)

        def __str__(self):
            return self.title


class  Sum(models.Model):
    '''huizong'''

    name = models.CharField(max_length=128, unique=True)
    create_num=models.IntegerField()
    update_num = models.IntegerField()

    def __str__(self):
        return self.name
