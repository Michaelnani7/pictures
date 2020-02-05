from django.urls import path
from . import views


urlpatterns =[
    path('create', views.create, name='create'),
    path('modeldetail', views.modeldetail, name='modeldetail'),
    path('album', views.album, name='album'),
    path('<int:model_id>', views.detail, name='detail'),
    path('<int:model_id>/upvote', views.upvote, name='upvote'),

]