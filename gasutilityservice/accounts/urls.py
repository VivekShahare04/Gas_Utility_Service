from django.urls import path
from .views import RegisterView, login_view, logout_view,account_landing

app_name = 'accounts'

urlpatterns = [
    path('', account_landing, name='landing'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]