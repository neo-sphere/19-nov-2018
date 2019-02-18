from django.urls import path

from django.contrib.auth.views import LoginView

from .views import signup, TransactionView

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('send/', TransactionView.as_view(), name="send"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
]
