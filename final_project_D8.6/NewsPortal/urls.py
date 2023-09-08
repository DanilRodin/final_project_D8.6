from django.urls import path
from .views import PostList, Event, NewsSearch, NewsCreate, NewsUpdate, NewsDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', Event.as_view(), name='post_detail'),
   path('search/', NewsSearch.as_view(), name='post_search'),

   path('create/', NewsCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),

   path('articles/create/', NewsCreate.as_view(), name='post_create'),
   path('articles/<int:pk>/edit/', login_required(NewsUpdate.as_view()), name='post_update'),
   path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
]
