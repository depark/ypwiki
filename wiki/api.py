from wiki.models import *
from django.core.exceptions import ObjectDoesNotExist


def lastdoc(aid):
    try:
        bdoc =Article.objects.get(id=int(aid ) -1)
    except ObjectDoesNotExist as e:
        bdoc =''

    # 下一篇
    try:
        adoc =Article.objects.get(id=int(aid ) +1)
    except ObjectDoesNotExist as e:
        adoc =''


    return bdoc,adoc