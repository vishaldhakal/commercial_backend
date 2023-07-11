from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('change-password/', views.ChangePasswordView.as_view(),
         name='change-password'),
    path("create-user-profile/", views.create_user_profile,
         name="create_user_profile"),
    path("verify-user-profile/", views.verify_user_profile,
         name="verify_user_profile"),
    path("get-user-profile/", views.get_user_profile, name="get_user_profile"),
    path("get-user-profile-detail/", views.get_user_profile_detail,
         name="get_user_profile_detail"),
    path("get-user-lists/", views.get_users, name="get_users"),
    path("get-user-detail/", views.get_user_detail, name="get_user_detail"),
    path("update-user-detail/", views.update_user_detail,
         name="update_user_detail"),
]
