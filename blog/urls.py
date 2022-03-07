from django.urls import path
from .views import HomeView,PostView,AddPost

app_name = "blog"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('add', AddPost.as_view(), name='add')
]
