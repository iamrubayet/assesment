from django.urls import path
from . import views as proxy_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", proxy_views.homePage , name = "home-page"),
    path("login/" , LoginView.as_view
         (template_name="proxymodelapp/loginPage.html") , name="login-user"),
    
]