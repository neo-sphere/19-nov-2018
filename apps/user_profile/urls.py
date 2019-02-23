from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from .views import TransactionView, SignUp

urlpatterns = [
    # path('signup/', signup, name="signup"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('send/', TransactionView.as_view(), name="send"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
