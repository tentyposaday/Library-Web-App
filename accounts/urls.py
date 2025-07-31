from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),  # 👈 login route
    path('logout/', views.logout_view, name='logout'),  # 👈 logout route (below)
]
