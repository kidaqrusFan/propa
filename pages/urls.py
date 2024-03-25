from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('detail1/', views.detail1, name='detail1'),
    path('detail2/', views.detail2, name='detail2'),
    path('detail3/', views.detail3, name='detail3'),
    path('detail4/', views.detail4, name='detail4'),
    path('detail5/', views.detail5, name='detail5'),
    path('detail6/', views.detail6, name='detail6'),
    path('about/', views.about, name='about'),
    path('property/', views.property, name='property')

]







