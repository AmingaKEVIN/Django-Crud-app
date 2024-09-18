
from django.urls import path
from app import views

urlpatterns = [
   path('',views.index,name="index"),
   path('about',views.about,name="about"),
    path('insert',views.insert,name="insert"),
     path('update/<id>',views.update,name="update"),
      path('delete/<id>',views.delete,name="delete"),
 path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
     path('logout/', views.logout_view, name='logout')
]
