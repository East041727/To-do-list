from django.urls import path
from .views import Homepage,create_something,update_something,delete_something,SignupView,LoginView,LogoutView

urlpatterns = [
    path('', Homepage, name='home' ),
    path('create/',create_something, name = 'create'),
    path('update/<slug:slug>/',update_something, name = 'update'),
    path('delete/<slug:slug>/',delete_something, name = 'delete'),
    path('signup/', SignupView, name='register'),
    path('login/', LoginView, name='login'),
     path('logout/', LogoutView, name='logout')

 



]