from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('checkview',views.checkview,name='checkview'),
    path('<str:room_name>/',views.room_disp,name="enter_room"),
    path('send',views.recieve_message,name='recieve_message'),
    path('get_messages/<str:room>/', views.get_message, name='getMessages'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),      
]