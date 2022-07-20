from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name= 'index'),
    path('add_member', views.addMember, name= 'add_member'),
    path('post_member', views.post_member, name= 'post_member'),
    path('detail/<int:id>', views.memberDetail, name= 'detail'),
    path('detail/add_comment/<int:idd>', views.addComment, name='add_comment'),
    path('detail/set_to_interviewed/<int:id>', views.interviewDone, name='set_to_interviewed')

]