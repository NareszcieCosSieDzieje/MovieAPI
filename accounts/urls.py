from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import registration_view, login_view, logout_view, AccountDetail, AccountList

app_name = 'accounts'

urlpatterns = [
    path('register/', registration_view, name="accounts-register"),
    path('login/', login_view, name="accounts-login"),
    path('logout/', logout_view, name="accounts-logout"),
    path('accounts/', AccountList.as_view(), name="accounts-list"),
    path('accounts/<int:pk>/', AccountDetail.as_view(), name="accounts-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
