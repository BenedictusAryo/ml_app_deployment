from django.conf.urls import url
from django.urls import path
from account_management import views  # SET THE NAMESPACE!
app_name = 'account_management'  # jangan lupa edit bagian ini, esuaikan app yang dibuat

urlpatterns=[
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]