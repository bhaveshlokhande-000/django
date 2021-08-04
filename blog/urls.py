from django.urls import path,include
from . import views

app_name='blog'

urlpatterns=[
    path('',views.home,name='homepage'),
    path('/blogs/',views.blog_list,name='blog_list'),
    path('blog/<int:author_id>/',views.blog,name='author_blog'),
    path('<int:blog_id>/',views.post_single,name='post_single'),
    path('bloggers/',views.author,name='author_list'),
    path('blogs/<int:index>/',views.paginate,name='paginate_blog'),
]