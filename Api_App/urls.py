from .views import RegisterAPI,LoginAPI
from django.urls import path
from knox import views as knox_views
from django.urls import path, include
from .views import getPhoneNumberRegistered, getPhoneNumberRegistered_TimeBased


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="otpgen"),
    path("time_based/<phone>/", getPhoneNumberRegistered_TimeBased.as_view(), name="OTP Gen Time Based"),

]
