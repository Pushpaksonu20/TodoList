from django.urls import path,include
from todoapp import views

urlpatterns=[
    path('',views.home,name="home"),
    path('update-task/<str:pk>/',views.updatetask,name='update'),
    path('delete-task/<str:pk>/',views.deleteTask,name='delete'),

    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('logout/',views.logoutPage,name="logout"),
    
]