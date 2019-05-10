from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def lst(request):
    return HttpResponse('Hello World')


# 视图函数
def article_content(request):
    article = Article.objects.all()[0]
    article_id = article.article_id
    title = article.title
    brief_content = article.brief_content
    content = article.content
    publish_date = article.date
    return_str = 'article_id:%s,title:%s,brief_content:%s,' \
                 'content:%s,publish_date:%s' % (article_id, title,
                                                 brief_content, content,
                                                 publish_date)
    return HttpResponse(return_str)


def get_index_page(request):
    all_article = Article.objects.all()
    return render(request, 'blog/index.html',
                  {
                      'article_list': all_article
                  })
