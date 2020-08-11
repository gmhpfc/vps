""" mysite url configration for blog app
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.post_list_view, name='post_list'),

	path('post/<int:pk>/', views.post_detail_view, name='post_detail'),

	path('post/new/', views.post_new_view, name='post_new'),
	# added to remove runtime error it work what is the diffrence in follwing code ?
	#path('post/edit/<int:pk>/', views.post_edit_view, name='post_edit'),
  	path('post/<int:pk>/edit/', views.post_edit_view, name='post_edit'),
]
