from django.urls import path, include
import blog.views

urlpatterns = [
    path('lst', blog.views.lst),
]
