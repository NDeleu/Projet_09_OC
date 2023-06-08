"""
URL configuration for LITReview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

import authentication.views
import rthome.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html',
    ), name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'
    ), name='password_change_done'),
    path('home/', rthome.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('profile-photo/upload/', authentication.views.upload_profile_photo,
         name='upload_profile_photo'),
    path('ticket/create/', rthome.views.create_ticket, name='create_ticket'),
    path('post-edit/', rthome.views.post_edit, name='post_edit'),
    path('ticket/<int:ticket_id>/edit/', rthome.views.edit_ticket,
         name='edit_ticket'),
    path('ticket/<int:ticket_id>/delete/', rthome.views.delete_ticket,
         name='delete_ticket'),
    path('ticket/create-with-review/', rthome.views.create_ticket_and_review,
         name='create_ticket_and_review'),
    path('ticket/<int:ticket_id>/review/create/', rthome.views.create_review,
         name='create_review'),
    path('ticket/<int:ticket_id>/error_review/', rthome.views.error_review,
         name='error_review'),
    path('ticket/<int:ticket_id>/error_change_ticket/',
         rthome.views.error_change_ticket,
         name='error_change_ticket'),
    path('ticket/<int:ticket_id>/review/<int:review_id>/error_change_review',
         rthome.views.error_change_review,
         name='error_change_review'),
    path('ticket/<int:ticket_id>/review/<int:review_id>/edit/',
         rthome.views.edit_review, name='edit_review'),
    path('ticket/<int:ticket_id>/review/<int:review_id>/delete/',
         rthome.views.delete_review, name='delete_review'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
