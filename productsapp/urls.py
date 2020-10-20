from django.urls import path
from. import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('add_post/', views.add_all_post, name="add_all_post"),
    path('about/', views.about, name="about"),
    path('blog/', views.post_list, name="post_list"),
    path('blog/<int:pk>/', views.post_content, name="post_content"),
    path('blog/add_post/', views.add_post, name="add_post"),
    path('blog/<int:pk>/edit/', views.post_content_edit, name="post_content_edit"),
    path('blog/<int:pk>/comment/', views.add_comments, name="add_comments"),
]