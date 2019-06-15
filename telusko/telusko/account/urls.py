from django.urls import path
# from . import views
from . import views
urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('select',views.select,name="select"),
    
    
]