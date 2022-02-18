from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),  # login page
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # change password urls
    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # reset password urls
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # for registration
    path('register/', views.register, name='register'),
    # for editing the profile
    path('edit/', views.edit, name='edit'),

    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail, name='user_detail'),

]

'''
you can replace all the above urls just by

from django.urls import path, include
# ...
urlpatterns = [
 # ...
 path('', include('django.contrib.auth.urls')),
]

because all the views are built_in views.
'''
