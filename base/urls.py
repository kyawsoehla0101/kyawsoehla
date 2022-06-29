from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('post/<str:pk>/',views.detailView, name='detail' ),
    path('category/<str:slug>/',views.categoryView, name='categorypost' ),
    path('tag/<str:slug>/',views.tagView, name='tag' ),
]
