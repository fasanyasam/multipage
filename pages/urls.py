from django.urls import path 
from .views import HomepageView, AboutView, LoginView

urlpatterns =[
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
]