from django.urls import path, include
import blog.views

urlpatterns = [
    path('lst', blog.views.lst),
    path('content', blog.views.article_content),
    path('index', blog.views.get_index_page)
]
