from django.urls import path
from .views import HomePage, Register, Login, addnew, edit, update, destroy, logoutuser, landinpage


urlpatterns = [
    path('', landinpage, name="land-page"),
    path('home/', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('addnew', addnew, name='addnew'),  
    path('edit/<int:id>', edit, name='edit'),  
    path('update/<int:id>', update, name='update'),  
    path('delete/<int:id>', destroy, name='destroy'), 
    path('logout/', logoutuser, name='logout'),
]
