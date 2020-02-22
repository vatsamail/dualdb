from django.urls import path
from blog import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('', views.content_index, name="content_index"),
    path("<int:pk>/", views.content_detail, name="content_detail"),
]
