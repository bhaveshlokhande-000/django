from django.urls import path,include
from . import views

app_name='blog'

urlpatterns=[
    path('',views.home,name='homepage'),
    path('author/',views.author,name='author_list'),
    path('blogs/<int:index>/',views.paginate,name='paginate_blog'),
    path('blog/<int:id>/',views.blog,name='author_blog'),
    path('<slug:post>/',views.post_single,name='post_single'),
   
]