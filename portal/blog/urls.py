from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_index, name="post_index"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path('test', views.test, name='test'),
    path('content/', views.content_index, name="content_index"),
    path("content/<int:pk>/", views.content_detail, name="content_detail"),

]
