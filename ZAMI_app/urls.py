from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('flowers/', views.flowers_page, name='flowers_page'),
    path('category/', views.category_page, name='category_page'),
    path('guides/', views.guides_page, name='guides_page'),
    path('flowers/detail/<int:pk>/', views.flowers_detail_page, name='flowers_detail_page'),
    path('guides/detail/<int:pk>/', views.guide_detail_page, name='guide_detail_page'),
    path('category/flowers/<slug:slug>/', views.flowers_by_category_page, name='flowers_by_category_page'),
    path('sign-up/',views.sign_up_page, name='sign_up_page'),
    path('login/',views.login_page, name='login_page'),
    path('logout/',views.logout_action, name='logout_action'),
]
